from tools import Tools

class Lang(Tools):
    def __init__(self):
        Tools.__init__(self)
       
        """
        English language lookup tools
        Word list from http://www-01.sil.org/Linguistics/wordlists/english/wordlist/wordsEn.txt
        (c) 2012, 2013 Intelligent Planet Ltd
        """
       
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        self.eng_dict = self.load('c:/python27/wordsEn.txt')
        self.freq = self.letter_frequency(self.eng_dict)

    
    def load(self, cfile):
        out = []
        file = open(cfile, 'rU')
        
        for row in file:
            if row: out.append(row.strip('\n'))
        
        return out
    
    
    def search(self, clist, txt): return [x for x in clist if txt in x]
    
    
    def filter(self, clist, txt):
        out = []
        
        for word in clist:
            test = 0
            
            for letter in word:
                if letter not in txt: test = 1
            
            if test == 0: out.append(word)
        
        return out
                

    def word_length(self, clist,  txt):
        out = []
        
        for word in clist:
            if len(word) <= len(txt): out.append(word)
        
        return out
    
    
    def combi(self, txt):
        out=self.eng_dict
        txt = self.order(txt)

        for item in txt:
            out = self.search(out, item)
            
        out = self.filter(out, txt)
        
        for letter in txt:
            out = self.letter_count(out, txt, letter)
            
        out = self.word_length(out, txt)
        
        end = len(txt)
        
        while len(out) == 0:
            end -= 1
            out = self.combi(txt[:end])
        return out
        
        
    def order(self, txt):
        out = ''
        
        for letter in self.freq:
            if letter in txt:
                while out.count(letter) < txt.count(letter): out += letter
            
        return out
            
    
    def letter_count(self, clist, txt, letter):
        out = []
        
        for word in clist:
            if word.count(letter) <= txt.count(letter): out.append(word)
        
        return out
    
    
    def letter_frequency(self, clist):
        out = []
        
        for letter in self.alphabet:
            res = len(self.search(clist, letter)), letter
            out.append(res)
        
        out.sort()
        outs = []
        
        for item in out:
            raw = item[1]
            outs.insert(0, raw)
        return outs
    
    

        
    
    
    
    
    
    
    

    
        
