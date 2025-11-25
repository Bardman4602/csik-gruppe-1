# Kan du lave et tupel, der har sig selv som element? Hvorfor ikke?

# Nej, fordi tuples er immutable og derfor ikke kan indeholde
# en reference til sig selv under konstruktion

# Visuelt eksempel:
t = ()
t += (t,)
print(t)