import requests

class MessageRouter:
    def __init__(self, zk_hosts='localhost:2181'):
        self.zk = KazooClient(hosts=zk_hosts)
        self.zk.start()
    
    def find_user_server(self, user_id):
        """Find which server a user is connected to"""
        try:
            user_path = f"/chat/users/{user_id}"
            data, stat = self.zk.get(user_path)
            user_location = json.loads(data.decode())
            return user_location
        except Exception as e:
            print(f"User {user_id} not found: {e}")
            return None
    
    def send_message(self, from_user, to_user, message):
        """Send message to a user (possibly on different server)"""
        # Find which server the recipient is on
        user_location = self.find_user_server(to_user)
        
        if not user_location:
            print(f"User {to_user} is offline")
            return False
        
        server_host = user_location['server_host']
        server_port = user_location['server_port']
        
        # Route message to that server
        try:
            response = requests.post(
                f"http://{server_host}:{server_port}/send_message",
                json={
                    "to_user": to_user,
                    "from_user": from_user,
                    "message": message
                }
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Failed to route message: {e}")
            return False
    
    def get_all_online_users(self):
        """Get list of all currently connected users"""
        try:
            users = self.zk.get_children("/chat/users")
            return users
        except Exception:
            return []
    
    def watch_user_status(self, user_id, callback):
        """Watch for when a specific user comes online/offline"""
        @self.zk.DataWatch(f"/chat/users/{user_id}")
        def user_watcher(data, stat):
            if stat is None:
                # User went offline
                callback(user_id, "offline", None)
            else:
                # User is online
                location = json.loads(data.decode())
                callback(user_id, "online", location)