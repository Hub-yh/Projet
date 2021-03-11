#!/usr/bin/.env python3

from book import Book

def main():
    book = Book("TEST")
    book.Inser_buy(10, 10.0)
    book.Inser_sell(120, 12.0)
    book.Inser_buy(5, 10.0)
    book.Inser_buy(2, 11.0)
    book.Inser_sell(1, 10.0)
    book.Inser_sell(10, 10.0)

if __name__ == "__main__":
    main()
