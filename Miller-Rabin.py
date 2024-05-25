from tkinter import *
from tkinter import messagebox
import random

# Colors
c1 = '#1C3F60'  # slightly dark
c2 = '#0B1320'  # dark
c3 = '#D9D9D9'  # like white

# Fonts
f1 = 'Arial 12 bold'
f2 = 'Arial 16 bold'
f3 = 'Arial 9 normal'

def main():
    root = Tk()
    root.geometry("500x450")
    root.configure(bg=c1)
    root.resizable(False, False)
    root.title("Miller-Rabin Primality Test")

    finalResult = ""
    
    # LABELS
    Label(root, text="Miller-Rabin Primality Test", bg=c1, fg=c3, font='Helvetica 24 bold').place(x=0, y=10, width=500)
    Label(root, text="No. to be tested", bg=c1, fg=c3, font=f3).place(x=40, y=105, width=140)
    Label(root, text="No. of iterations", bg=c1, fg=c3, font=f3).place(x=200, y=105, width=140)
    Label(root, text="RESULT:", font=f2, bg=c3, fg=c2).place(x=40, y=135, width=140, height=35)
    resultLabel = Label(root, text=finalResult, font=f2, bg=c2, fg=c3)
    resultLabel.place(x=180, y=135, width=275, height=35)
    Label(root, text="PROCESS", font=f2, fg=c2, bg=c3).place(x=40, y=190, width=415, height=30)

    # ENTRY
    numValue = StringVar()  # Number to be tested
    iterationValue = StringVar()  # Number of iterations
    num = Entry(root, textvariable=numValue, bd=1, font=f1, bg=c2, fg=c3, justify='center')
    num.place(x=40, y=70, width=140, height=35)
    num.config(insertbackground=c3)
    iter = Entry(root, textvariable=iterationValue, bd=1, font=f1, bg=c2, fg=c3, justify='center')
    iter.place(x=200, y=70, width=140, height=35)
    iter.config(insertbackground=c3)

    processText = Text(root, bd=1, font=f1, bg=c2, fg=c3)
    processText.place(x=40, y=221, width=415, height=200)
    processText.tag_configure("center", justify="center")

    def check():
        processText.config(state=NORMAL)
        n = int(numValue.get())
        k = int(iterationValue.get())

        if n == "" or k == "":
            messagebox.showwarning("Missing Information", "Please fill in all the fields.")
            return
        else:
            processText.delete("1.0", END)  # Clear previous process text
            processText.insert(END, f"Number being tested: {n}\n")
            processText.insert(END, f"No. of Iterations: {k}\n")
            
            if is_prime(n, k, processText):
                finalResult = 'PROBABLY PRIME'
            else:
                finalResult = 'COMPOSITE'
            
            resultLabel.config(text=finalResult)
            processText.config(state=DISABLED)
            
    Button(root, text="CHECK", bd=1, font=f1, bg=c3, fg=c2, command=check).place(x=355, y=71, width=100, height=35)

    root.mainloop()


def is_prime(n, k, processText):
    if n <= 1 or n == 4:
        processText.insert(END, f"\nSince {n} <= 1 or {n} = 4, it is composite and no need to proceed for testing.\n")
        return False
    if n <= 3:
        processText.insert(END, f"\nSince {n} = 2 or {n} = 3, it is prime and no need to proceed for testing.\n")
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for i in range(k):
        processText.insert(END, f"\nIteration {i+1}:\n")
        processText.insert(END, f"d = {d}\n")
        if not millerRabin_test(d, n, processText):
            return False
    return True


def millerRabin_test(d, n, processText):
    a = 2 + random.randint(0, n - 2)
    x = power(a, d, n)
    processText.insert(END, f"a = {a}\n")
    processText.insert(END, f"x = {a}^{d} mod {n} = {x}\n")
    if x == 1 or x == n - 1:
        processText.insert(END, "RESULT: PROBABLE PRIME\n")
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            processText.insert(END, "RESULT: COMPOSITE\n")
            return False
        if x == n - 1:
            processText.insert(END, "RESULT: PROBABLE PRIME\n")
            return True
    processText.insert(END, "RESULT: COMPOSITE\n")
    return False


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res


main()
