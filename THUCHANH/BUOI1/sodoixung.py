def kiem_tra_so_doi_xung(n):
  str_n = str(n)
  str_n = str_n[::-1]
  return str_n == str(n)
def main():
  n = int(input())
  is_palindrome = kiem_tra_so_doi_xung(n)
  if is_palindrome:
    print("true")
  else:
    print("false")
if __name__ == "__main__":
  main()