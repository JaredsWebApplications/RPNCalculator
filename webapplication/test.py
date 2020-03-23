from backend import main
expr_ = "1 2 +"
main.rpn_calculator(expr_)
if(not main.stack_.is_empty()):
  try: print("\t{0:.15f}".format(main.stack_.peek()))
  except IndexError: print("\tstack is empty")
main.stack_.clear_contents()
