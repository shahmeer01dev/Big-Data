# main.py
import requests
from hdfs import InsecureClient

# Create a custom session class to handle the Docker network address translation.
class LocalResolverSession(requests.Session):
    def resolve(self, host):
        # This function forces any hostname (like 'datanode') to be
        # resolved as 'localhost', which is what we need.
        return 'localhost'

def hdfs_crud_operations():
    """
    Connects to HDFS via WebHDFS and performs CRUD operations.
    """
    try:
        # Pass an instance of our custom session to the client.
        client = InsecureClient('http://localhost:9870', user='root', session=LocalResolverSession())
        print("✅ Successfully connected to HDFS via WebHDFS.")

        # Define paths and content
        dir_path = "/user/test_dir_webhdfs"
        file_path = f"{dir_path}/my_file_web.txt"
        initial_content = "Hello from the WebHDFS client!\nThis is the first line.\n"
        append_content = "This is an appended line.\n"

        # === 1. CREATE Operations ===
        print("\n--- Performing CREATE operations ---")
        client.makedirs(dir_path)
        print(f"Directory '{dir_path}' created.")

        with client.write(file_path, encoding='utf-8', overwrite=True) as writer:
            writer.write(initial_content)
        print(f"File '{file_path}' created with initial content.")

        # === 2. READ Operation ===
        print("\n--- Performing READ operation ---")
        with client.read(file_path, encoding='utf-8') as reader:
            content = reader.read()
            print(f"Reading content from '{file_path}':\n---\n{content.strip()}\n---")

        # === 3. UPDATE Operation (Append) ===
        print("\n--- Performing UPDATE operation (Append) ---")
        with client.write(file_path, encoding='utf-8', append=True) as writer:
            writer.write(append_content)
        print(f"Appended content to '{file_path}'.")

        # Verify the update by reading again
        print("Verifying updated content:")
        with client.read(file_path, encoding='utf-8') as reader:
            updated_content = reader.read()
            print(f"---\n{updated_content.strip()}\n---")

        # === 4. DELETE Operations ===
        print("\n--- Performing DELETE operations ---")
        client.delete(dir_path, recursive=True)
        print(f"Directory '{dir_path}' and its contents deleted.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    hdfs_crud_operations()