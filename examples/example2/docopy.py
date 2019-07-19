from shutil import copyfile

folder_src = "/home/elle/Dropbox/Work/PresentazioniArticoli/2019/Articles/dfn_transport/tipetut++/Results/example2/img/"
folder_dist = "/home/elle/Dropbox/Work/PresentazioniArticoli/2019/Articles/dfn_transport/tipetut++/Article/Parts/Images/"

figures = [
"example2_coarse_mismatch_OPTfem.pdf",
"example2_coarse_mismatch_OPTxfem.pdf",
"example2_coarse_outflow.pdf",
"example2_coarse_cot_avg_frac_3.pdf",
"example2_coarse_cot_avg_frac_1.pdf",
"example2_fine_cot_avg_frac_1.pdf",
"example2_fine_cot_avg_frac_3.pdf",
"example2_fine_mismatch_OPTfem.pdf",
"example2_fine_outflow.pdf",]

for figure in figures:
    copyfile(folder_src + figure, folder_dist + figure)
