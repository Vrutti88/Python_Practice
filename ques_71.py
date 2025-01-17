# Q71) Write a recursive solution to the Tower of Hanoi puzzle for n disks.Write a recursive solution to the Tower of Hanoi puzzle for n disks.
def tower(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower(n-1, auxiliary, source, destination)
n = int(input("Enter the number of disks: "))
tower(n, 'A', 'B', 'C')
