def main():
    toys = [
        EngineDriver("large"),
        Gardener("small"),
        BankManager("medium"),
        Clown("large")

    ]
    for toy in toys:
        toy.talk()

if __name__ == "__main__":
    main()