import asyncio
import asyncssh

ASCII_MESSAGE = r"""

Amal says hi to

 Badri
 Aarif
 Darshan
 Mukundan
 Vidip
 Harish

"""

class HelloServer(asyncssh.SSHServer):
    def begin_auth(self, username):
        return False   # Disable all authentication

    def session_requested(self):
        return HelloSession()


class HelloSession(asyncssh.SSHServerSession):
    def session_started(self):
        self._chan.write(ASCII_MESSAGE)
        self._chan.exit(0)


async def main():
    await asyncssh.listen(
        host="0.0.0.0",
        port=22,                # Railway will map this to a public port
        server_factory=HelloServer
    )
    await asyncio.Future()     # Keep running


if __name__ == "__main__":
    asyncio.run(main())
