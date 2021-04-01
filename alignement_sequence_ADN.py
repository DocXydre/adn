##############################
#TP2 alignement de séquence###
##############################

####################
#EX 1 force brute###
####################

def souschaine(str1) :
    """renvoie la liste des sous-chaine de str1
    precondition :
        str1 type str
    postcondition :
        return type list
    Exemple :
    >>> souschaine('BON')
    ['B','O', 'N', 'BO', 'ON', 'BON']
    """
    pass

def est_souschaine(str2,substr):
    """docstring à faire"""
    i=0
    j=-1
    n = len(substr)
    n2 = len(str2)
    while i < n :
        c = strbstr[i]
        j+=1
        while j < n2 and str2|j]!=c :
            j+=1
        if j == n2 :
            return False
        i+=1
    return True

def alignement_sequence(str1,str2) :
    """docstring à faire"""
    pass

###################################
#ex2 avec programmation dynamique##
###################################

def aligne(s1,s2) :
    """renvoie le meileur score d'alignement entre s1 et s2"""
    n1 = len(s1)
    n2 = len(s2)
    #initialisation du tableau score rempli de 0 de taille (n1+1) x (n2+1)
    #exemple pour s1 = 'BO' et s2 ='JOUR' on veut :
    #score = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    score = ...
    #remplir la première ligne et la première colonne sachant que cela signifie que l'une des deux séquence est vide
    for i in range(n1+1) :
        score[i][0] = ...
    for j in range(n2+1) :
        score[0][j] =...
    #remplissage du reste du tableau
    for i in range(1,n1+1) :
        for j in range(1,n2+1) :
            #pour chaque case score[i][j], il s'&git de calculer le score max
            #pour aligner les mots s1[0:i] et s2[0:j] il y a trois cas selon l'alignement du dernier caractère
            #pour le cas où le dernier caractère est alogné avec '-'
            #Le score est alors obtenu avec un point de pénalité et l'alignement maximal,
            #déjà calculé, pour un mot raccourci d'un caractère,
            #c'est-à-dire soit sc[i-1][j],  soit sc[i][j-1].
            s = max(...,...)
            #reste alors le cas où les deux derniers caractères sont alignés.
            #Dans ce cas, on marque un point si les caractères coïncident et on perd un point sinon.
            if s1[i-1] == s2[j-1] :
                sc[i][j] = max(s, ...)
            else :
                sc[i][j] = max(s, ...)
    #Une fois sorti de la double boucle, le tableau est correctement rempli.
    #Il ne reste plus qu'à renvoyer la valeur située dans la toute dernière case,
    #qui correspond au score d'alignement des deux mots complets.
    return sc[n1][n2]
            
#tests avec 'GENOME' et 'ENORME'    
        
