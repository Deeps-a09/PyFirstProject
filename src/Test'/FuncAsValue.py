def greetings(name):
    def hello():
        return name
    return hello


greet = greetings("Atlantis!")
print(greet())
