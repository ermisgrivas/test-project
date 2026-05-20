import math  # Βιβλιοθήκη της Python που χρησιμοποιείται για το παραγοντικό (factorial)


def find_dyck_paths(num, x=0, y=0, path=""):
    if x == num and y == num:
        return [path.rstrip(",")]  # Ολοκλήρωση μονοπατιού
    paths = []
    if x < num:
        paths += find_dyck_paths(num, x + 1, y, path + "Up,")  # Αν το x βρίσκεται κάτω από το num πάμε προς τα πάνω
    if x > y:
        paths += find_dyck_paths(num, x, y + 1, path + "Right,")  # Αν το x βρίσκεται πάνω από το y πάμε προς τα δεξιά
    return paths  # Στο τέλος επιστρέφουμε τον πίνακα


def catalan(num: int) -> int:  # Συνάρτηση υπολογισμού του αριθμού Catalan ενός ακεραίου num
    if num <= 1:
        return 1
    else:
        return int(math.factorial(2 * num) / ((num + 1) * math.factorial(num) * math.factorial(num)))


n = int(input("Enter n: "))
print("A " + str(n) + "x" + str(n) + " grid has " + str(catalan(n)) + " Dyck paths.\n")
print("Here's a list of all " + str(catalan(n)) + " Dyck paths:")
print(find_dyck_paths(n))
