# -*- coding: utf-8 -*-
"""
This module provides the following functions:
file_reader() - reads a secquence of files and returns
list of all words present in all the files.

histogram() - finds and returns the frequency of each
present in the given secquence of words.

write_in_file() - writes content into a file
depending on the type of content.

This is a part of the exercises given under the 
course UIT2211 (Software Development Project - I).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Thur Apr 13 2023

Revised on Tue Apr 18 2023

Original Author: S.Shiva sai adithiyan <shivasaiadithiyan2210687@ssn.edu.in>

"""


def file_reader(secq_of_file_paths):
    """

    Reads all the files given as a secquence of 
    file paths and returns a secquence 
    of words present in all the files.
    if the given secq is empty 
    return value is empty secquence.

    The input secquence is not modified and there are no side effects.
    
    secq_of_file_paths: A secquence of indexed objects
    containing file paths.

    returns: list of words if secq_of_file_paths
    is empty otherwise empty list. 
    
    """
    secq_of_file_paths=list(secq_of_file_paths)
    secq_of_words=[]
    #opening files in encoding utf-8
    for path in secq_of_file_paths:
        file_handle=open(path,"r",encoding = "utf-8")
        line=1
        while line:
            line=file_handle.readline()
            words=line.split()
            
            for word in words:
                if word.isalnum() or word.isnumeric() or word.isalpha():
                    secq_of_words.append(word)
        file_handle.close()

    return secq_of_words




def histogram (secquene_of_words):
    """
    finds and returns the frequency of each
    word present in the secquence of words.

    The input secquence is not modified and there are no side effects.

    secquence_of_words: A secquence of indexed objects
    containing words.

    returns: dictionary with word as key and frequency
    of that word as value.
    if secquence_of_words is empty returns 
    empty dictionary.


    """
    word_frequency={}
    for word in secquene_of_words:
        if word not in word_frequency:
            word_frequency[word]=1
        else:
            word_frequency[word]+=1
    
    return word_frequency





def write_in_file(file_name,content):
    """
    writes content into a file according to the
    type of content given.

    The input secquence is not modified and there are no side effects.

    file_name: file name along with path to which
    content must be written.

    content: writes key:value in each line if content type
    is dictionary.
    writes words with blank spaces if content type is a list.

    returns: True if content has been written into file
    otherwise False.

    """


    file_handle=open(file_name,"w",encoding="utf-8")
    if type(content) is dict:
        content=list(content.items())
        for item in content:
            file_handle.write(f"{item[0]}:{item[1]}")
            file_handle.write("\n")
        file_handle.close()
        return True
    elif type(content) is list:
        for word in content:
            file_handle.write(word)
            file_handle.write(" ")
        file_handle.close()
        return True
    
    else:
        return False




import glob
if __name__=="__main__":
    
    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    path=r"S:/Python_files_SEM_2/SDL/python-3.11.3-docs-text/**/*.txt"
    
    #the glob method of glob module iterates through all the files searching
    #for a specific pattern of file (in this case a txt file).
    files=glob.glob(path,recursive=True)
    
    all_words=file_reader(files)

    writing_in_file=write_in_file("words.txt",all_words)

    word_frequency=histogram(all_words)

    #sorting the dict according to frequency(key).
    word_frequency_sorted=dict(sorted(word_frequency.items(),key=lambda x:x[1],reverse=True))

    writing_in_file_2=write_in_file("words-histogram.txt",word_frequency_sorted)

    while True:
        try:
            while True:
                secq_of_words_with_same_prefix=[]
                user_prefix_input=input("Enter a prefix: ")
                if user_prefix_input =="":
                    raise ValueError
                for word in word_frequency_sorted:
                    if word.startswith(user_prefix_input):
                        secq_of_words_with_same_prefix.append(word)
                
                print(f"The words which have {user_prefix_input} as prefix are: ")
                print(secq_of_words_with_same_prefix)
            
            
        #programs quits when ctrl+c is pressed.
        except KeyboardInterrupt :
            print()
            print("-"*25)
            print("Program Aborted.") 
            print("-"*25)
            break

        #program quits when ctrl + z + return is pressed.
        except EOFError:
            print("-"*25)
            print("Program Aborted.") 
            print("-"*25)
            break

        #when invalid input is given program
        #display the below.
        except ValueError:
            print()
            print("!!!Pls enter valid prefix!!!")
            