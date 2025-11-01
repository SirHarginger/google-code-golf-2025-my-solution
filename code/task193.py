p=lambda g,L=len,E=enumerate:[[v*((i and g[i-1][j]==v)+(i+1<L(g)and g[i+1][j]==v)+(j and r[j-1]==v)+(j+1<L(r)and r[j+1]==v)>1)for j,v in E(r)]for i,r in E(g)]
