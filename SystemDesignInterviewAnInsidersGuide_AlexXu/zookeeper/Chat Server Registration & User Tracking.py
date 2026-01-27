from kazoo.client import KazooClient
import json
import socket

class ChatServer:
    def __init__(self, server_id, zk_hosts='localhost:2181'):
        self.server_id = server_id
        self.server_host = socket.gethostbyname(socket.gethostname())
        self.server_port = 8080
        
        # Connect to ZooKeeper
        self.zk = KazooClient(hosts=zk_hosts)
        self.zk.start()
        
        # Track local WebSocket connections
        self.active_connections = {}  # {user_id: websocket_connection}
        
        # Initialize ZK structure
        self.zk.ensure_path("/chat/servers")
        self.zk.ensure_path("/chat/users")
        
        # Register this server
        self.register_server()
    
    def register_server(self):
        """Register this chat server in ZooKeeper"""
        server_info = json.dumps({
            "server_id": self.server_id,
            "host": self.server_host,
            "port": self.server_port,
            "status": "active"
        })
        
        # Ephemeral node - auto-deleted if server crashes
        self.zk.create(
            f"/chat/servers/{self.server_id}",
            server_info.encode(),
            ephemeral=True
        )
        print(f"Server {self.server_id} registered at {self.server_host}:{self.server_port}")
    
    def on_user_connected(self, user_id, websocket):
        """Called when a user establishes WebSocket connection"""
        # Store connection locally
        self.active_connections[user_id] = websocket
        
        # Register user location in ZooKeeper
        user_location = json.dumps({
            "user_id": user_id,
            "server_id": self.server_id,
            "server_host": self.server_host,
            "server_port": self.server_port,
            "connected_at": time.time()
        })
        
        # Ephemeral node - auto-deleted if connection drops
        self.zk.create(
            f"/chat/users/{user_id}",
            user_location.encode(),
            ephemeral=True
        )
        print(f"User {user_id} connected to server {self.server_id}")
    
    def on_user_disconnected(self, user_id):
        """Called when user's WebSocket closes"""
        # Remove from local tracking
        if user_id in self.active_connections:
            del self.active_connections[user_id]
        
        # Remove from ZooKeeper
        try:
            self.zk.delete(f"/chat/users/{user_id}")
            print(f"User {user_id} disconnected from server {self.server_id}")
        except Exception as e:
            print(f"Error removing user {user_id}: {e}")
    
    def send_local_message(self, user_id, message):
        """Send message to a user connected to THIS server"""
        if user_id in self.active_connections:
            websocket = self.active_connections[user_id]
            websocket.send(message)
            return True
        return False