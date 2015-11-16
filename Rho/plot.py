import matplotlib.pyplot as plt

def plot(x, y, err, fmts, colors):
    plt.errorbar(x, y, yerr=err, fmt=fmts.next(), color=colors.next(), mec='white')
    plt.semilogx()
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    
if (__name__=="__main__"):
    pass