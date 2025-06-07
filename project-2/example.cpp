#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main()
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0)
    {
        std::cerr << "Socket creation failed: " << strerror(errno) << std::endl;
        return 1;
    }

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(5550);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    std::cout << "Attempting to connect to 127.0.0.1:5550..." << std::endl;
    int result = connect(sock, (sockaddr *)&server_addr, sizeof(server_addr));
    if (result < 0)
    {
        std::cerr << "Connection failed: " << strerror(errno) << std::endl;
        close(sock);
        return 2;
    }

    std::cout << "Connection successful!" << std::endl;
    close(sock);
    return 0;
}