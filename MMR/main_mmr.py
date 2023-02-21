import mmr_summarize
import os

mmr = mmr_summarize.mmr_summarize()
summary_length = 45 # Summary will contain more or less 50 sentences, due to the algorithm's small variance in the amount of selected sentences
summary = []
query_length = 10
summ_Folder = "/content/drive/MyDrive/Proj_PFC/MMR/summaries/"
Root_Folder = "/content/drive/MyDrive/Proj_PFC/MMR/documents/"
Directory_List = next(os.walk(Root_Folder))[1]
for Directory in Directory_List:
    data = ""
    Current_Dir = os.path.join(Root_Folder, Directory)
    Current_Dir += "/"
#    print(Current_Dir)
    for root_dir, dirs, files in os.walk(Current_Dir):

        data = ""
        summary = mmr.main(query_length, summary_length, root_dir)          
        for sent in summary:
            data +=  sent.getOGwords() + "\n"

        FileName = summ_Folder +Directory+ "_MMR.txt"
        print(FileName)
        write_to_file = open(FileName, "w")
        write_to_file.write(data)
        write_to_file.write("\n")
        write_to_file.close()
            
                



