# Repl to run CSC201 demos in
# Peter Brown <peter.brown@converse.edu>, 2020-01-12

from typing import List

import chaos
import chaos_clamped
import covid_graph
import covid_graph_coords
import CtoF
import graphicsdemo
import fact
import futureval
import futureval_clamped
import pounds_to_stone
import quadratic
import rangedemo
import sumlist

def main(args:List[str]) -> int:
    return covid_graph_coords.main(args)

if __name__ == '__main__':
    import sys
    main(sys.argv)