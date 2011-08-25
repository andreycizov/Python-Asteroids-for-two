import pstats
p = pstats.Stats('fooprof')
p.sort_stats('cumulative').print_stats()
p.sort_stats('cumulative').print_callers(.1)

