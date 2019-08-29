import search 
from search import UndirectedGraph, breadth_first_graph_search, greedy_best_first_graph_search

from search import * #semua kelas keambil

romania_map = UndirectedGraph(dict(										#jarak kota yang saling adjacent
    Manchester = dict(Liverpool=30, Sheffield=40),
	Liverpool = dict(Nottingham=110, Shrewsbury=70),
	Sheffield = dict(Nottingham=40),
	Shrewsbury = dict(Bham=50, Aberystwyth=80, Cardiff=110),
	Nottingham = dict(Bham=50, Oxford=100),
	Bham = dict(Oxford=70, Bristol=90),
	Aberystwyth = dict(Cardiff=120),
	Oxford = dict(Southampton=70),
	Cardif = dict(Bristol=50),
	Bristol = dict(Southampton=80)
	))
	
    
romania_problem = GraphProblem('Manchester', 'Southampton', romania_map)	#romania map jalur efektif dari state awal ke state akhir



#mau pake bfs
a=[node.state for node in breadth_first_graph_search(romania_problem).path()]
print(a)

#mau pake dfs
a=[node.state for node in depth_first_graph_search(romania_problem).path()]
print(a)



#kalo inform kita tau jarak pasti di petanya 
#kalo uninform hanyak diketahui jarak antar kota


	

