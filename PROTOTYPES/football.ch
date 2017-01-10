@x l.61
main(argc,argv)
  int argc; /* the number of command-line arguments */
  char *argv[]; /* an array of strings containing those arguments */
@y
int main(@t\1\1@>
  int argc, /* the number of command-line arguments */
  char *argv[]@t\2\2@>) /* an array of strings containing those arguments */
@z

@x l.140
Vertex *prompt_for_team(s)
  char *s; /* string used in prompt message */
@y
Vertex *prompt_for_team(char *s)
  /* string used in prompt message */
@z

@x
    fgets(buffer,30,stdin);
@y
    if (fgets(buffer,30,stdin)) {}
@z

@x l.207
node *new_node(x,d)
  node *x; /* an old node that the new node will call |prev| */
  long d; /* incremental change to |tot_len| */
@y
node *new_node(@t\1\1@>
  node *x, /* an old node that the new node will call |prev| */
  long d@t\2\2@>) /* incremental change to |tot_len| */
@z

@x
    register Arc *best_arc; /* arc that achieves |del=d| */
    register Arc *last_arc; /* arc that goes directly to |goal| */
@y
    register Arc *best_arc=0; /* arc that achieves |del=d| */
    register Arc *last_arc=0; /* arc that goes directly to |goal| */
@z

@x
      if (a->del>d && a->tip->valid==v)
        if (a->tip==goal) last_arc=a;
        else best_arc=a,d=a->del;
@y
      if (a->del>d && a->tip->valid==v) {
        if (a->tip==goal) last_arc=a;
        else best_arc=a,d=a->del;
      }
@z
