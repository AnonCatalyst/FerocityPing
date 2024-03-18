

🌐 **FerocityPing: A Python Network Utility**

FerocityPing is a Python network utility designed to ping hosts using multiple methods and retrieve location information. It offers ICMP, UDP, TCP, and HTTP ping functionalities to assess connectivity and response times.

**Features:**

1️⃣ **ICMP Ping:** Uses the ICMP protocol to send echo requests to the target host and measures the round-trip time for the responses. This method is commonly used for basic network connectivity testing.

2️⃣ **UDP Ping:** Sends an empty UDP packet to the specified port of the target host and waits for a response. This method provides an alternative to ICMP ping and can be useful for testing UDP-based services.

3️⃣ **TCP Ping:** Attempts to establish a TCP connection to the specified port of the target host. If successful, it considers the ping successful. This method is useful for testing TCP-based services.

4️⃣ **HTTP Ping:** Sends an HTTP GET request to the specified URL and checks the response status code. This method is helpful for testing web servers and web applications.

**Location Information:**

FerocityPing also provides location information for the target host by resolving its IP address and querying the ipinfo.io API. This information includes the city, region, country, and coordinates of the host.

**Usage:**

1️⃣ Upon running the script, users are prompted to enter the target hostname or IP address and the port to ping.

2️⃣ Users can choose whether to perform an endless ping or a single ping attempt.

3️⃣ The script then executes the selected ping method and displays the result, including success or failure status and response time.

4️⃣ In case of failure, FerocityPing attempts alternative methods to ping the host, such as UDP, TCP, and HTTP.

5️⃣ The script handles various exceptions, including invalid input, ping command errors, keyboard interrupts, and unexpected errors.

**How to Use:**

1️⃣ Ensure Python is installed on your system.

2️⃣ Download the FerocityPing script and save it as a `.py` file.

3️⃣ Open a terminal or command prompt and navigate to the directory containing the script.

4️⃣ Run the script by executing `python FerocityPing.py`.

5️⃣ Follow the prompts to enter the target hostname or IP address, port, and desired ping method.

6️⃣ Review the ping results and location information provided by the script.

7️⃣ Press `Ctrl+C` to stop an endless ping or follow the on-screen instructions to exit.

**Note:** Ensure that you have permission to ping the target host and that the necessary network connectivity is available for accurate results.

