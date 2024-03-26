#-------------------------------------------------------------------

Offer = DiscreteDistribution({'grad':0.9, 'no-grad':0.1})

Tester = ConditionalProbabilityTable([
   ['cancer', 'positive', 0.9],
   ['cancer', 'negative', 0.1], 
   ['no-cancer', 'positive', 0.2],
   ['no-cancer', 'negative', 0.8]], [Offer])

s_cancer = State(Offer, 'disease')
g_o1 = State(Tester, 'o1')
g_o2 = State(Tester, 'o2')

model = BayesianNetwork('disease')

model.add_states(s_cancer, g_o1, g_o2)

model.add_transition(s_cancer, g_o1)
model.add_transition(s_cancer, g_o2)

model.bake() # finalize the topology of the model

print ('The number of nodes:', model.node_count())
print ('The number of elges:', model.edge_count())

# predict_proba(Given factors)
# P(pos | c) and P(neg | c)
print (model.predict_proba({'o1':'positive', 
   'o2':'positive'})[0].parameters)

# P(c | + -) and P(~c | + -)
print (model.predict_proba({'o1':'positive', 
   'o2':'negative'})[0].parameters)

# P(t2 = pos | t1 = pos) and P(t2 = neg | t1 = pos)
print (model.predict_proba({'o1':'positive'})[2].parameters)