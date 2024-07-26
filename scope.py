def inner():
    a = "inner"

def outer():
    a = "outer"
    inner()
    print(a)

def main() -> bool:
    print("Hello World.")
    outer()
    return True

# Running this file will call the main() function like an entrypoint as per convention familiar to C programs
if __name__ == "__main__":
    main()