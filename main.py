import gitRepositoryHandler
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        actions = self.path.split('/')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>gitHub Handler</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))

        if (len(actions) != 3):
            self.wfile.write(bytes("wrong parameters number <br>", "utf-8"))
            self.wfile.write(bytes("please insert url http://localhost:8000/github_username/command <br>", "utf-8"))
            self.wfile.write(bytes("acceptable commands: <br>", "utf-8"))
            self.wfile.write(bytes("repositories - to list github user repositories <br>", "utf-8"))
            self.wfile.write(bytes("total_stars - to show users total stars <br>", "utf-8"))

        elif (actions[2] == "repositories"):
            githandler = gitRepositoryHandler.gitUser(actions[1])
            repoList = githandler.listRepositories()
            for row in repoList:
                self.wfile.write(bytes(row, "utf-8"))
                self.wfile.write(bytes("<br>", "utf-8"))

        elif (actions[2] == "total_stars"):
            githandler = gitRepositoryHandler.gitUser(actions[1])
            totalStars = githandler.getTotalStars()
            self.wfile.write(bytes("user total stars: " + totalStars, "utf-8"))

        else:
            self.wfile.write(bytes("command not found <br>", "utf-8"))
            self.wfile.write(bytes("please insert url http://localhost:8000/github_username/command <br>", "utf-8"))
            self.wfile.write(bytes("acceptable commands: <br>", "utf-8"))
            self.wfile.write(bytes("repositories - to list github user repositories <br>", "utf-8"))
            self.wfile.write(bytes("total_stars - to show users total stars <br>", "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
