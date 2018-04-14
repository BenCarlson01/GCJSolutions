#Ben Carlson
import subprocess

def test1():
    Cases = 4
    print(str(Cases), file = p.stdin)
    print("3 6 1 1", file = p.stdin)
    print(".@@..@", file = p.stdin)
    print(".....@", file = p.stdin)
    print("@.@.@@", file = p.stdin)


    print("4 3 1 1", file = p.stdin)
    print("@@@", file = p.stdin)
    print("@.@", file = p.stdin)
    print("@.@", file = p.stdin)
    print("@@@", file = p.stdin)


    print("4 5 1 1", file = p.stdin)
    print(".....", file = p.stdin)
    print(".....", file = p.stdin)
    print(".....", file = p.stdin)
    print(".....", file = p.stdin)


    print("4 4 1 1", file = p.stdin)
    print("..@@", file = p.stdin)
    print("..@@", file = p.stdin)
    print("@@..", file = p.stdin)
    print("@@..", file = p.stdin)


    print("3 4 2 2", file = p.stdin)
    print("@.@@", file = p.stdin)
    print("@@.@", file = p.stdin)
    print("@.@@", file = p.stdin)


    print("3 4 1 2", file = p.stdin)
    print(".@.@", file = p.stdin)
    print("@.@.", file = p.stdin)
    print(".@.@", file = p.stdin)

    print(p.stdout.read())

def test2():
    print("3", file = p.stdin)
    print("2 2 2", file = p.stdin)
    print("1 2 3", file = p.stdin)
    print("1 1 2", file = p.stdin)

    print("2 2 2", file = p.stdin)
    print("1 2 3", file = p.stdin)
    print("2 1 2", file = p.stdin)
    
    print("3 4 5", file = p.stdin)
    print("2 3 3", file = p.stdin)
    print("2 1 5", file = p.stdin)
    print("2 4 2", file = p.stdin)
    print("2 2 4", file = p.stdin)
    print("2 5 1", file = p.stdin)

    print(p.stdout.read())

def test3():
    Cases = 4
    print(str(Cases), file = p.stdin)
    print("1 7", file = p.stdin)
    print("1 1", file = p.stdin)

    print("2 920", file = p.stdin)
    print("50 120", file = p.stdin)
    print("50 120", file = p.stdin)

    print("1 32", file = p.stdin)
    print("7 4", file = p.stdin)

    print("2 604", file = p.stdin)
    print("1 100", file = p.stdin)
    print("1 100", file = p.stdin)

    print("3 240", file = p.stdin)
    print("10 20", file = p.stdin)
    print("20 30", file = p.stdin)
    print("30 10", file = p.stdin)

    print(p.stdout.read())



p = subprocess.Popen(
	  ["python", "Round1A3.py"],
	  stdin=subprocess.PIPE,
	  stdout=subprocess.PIPE,
	  bufsize=1,
	  universal_newlines=True)
test3()

