# Print the valid parenthis pair of the given number.
# sp=> starting pare, ep=> closing paren
def print_balanced_parathensis(sp, ep, string):
    if sp == 0 and ep == 0:
        print (string)
    if sp > ep:
        return
    if sp > 0 :
        print_balanced_parathensis(sp-1, ep, string+"(")
    if ep > 0 :
        print_balanced_parathensis(sp, ep-1, string+")")
        
print (print_balanced_parathensis(4, 4, ""))
