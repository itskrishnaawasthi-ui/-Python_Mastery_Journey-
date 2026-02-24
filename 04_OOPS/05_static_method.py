#Methods that don't use self parameter (work at class level).
#decorator: allow us to wrap another function in order to extend the behaviour of hte wrapped function , without permanently modifying it.
class student:
    @staticmethod #decorator
    def classes():
        print("ABRA KA DABRA")

s=student()
s.classes()
