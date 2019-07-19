from shutil import copyfile

folder_src = "/home/elle/Dropbox/Work/PresentazioniArticoli/2019/Articles/dfn_transport/tipetut++/Results/example1/img/"
folder_dist = "/home/elle/Dropbox/Work/PresentazioniArticoli/2019/Articles/dfn_transport/tipetut++/Article/Parts/Images/"

figures = [
"example1_coarse_cot_avg_0_frac_0.pdf",
"example1_coarse_cot_avg_0_frac_1.pdf",
"example1_coarse_cot_avg_10_frac_0.pdf",
"example1_coarse_cot_avg_10_frac_1.pdf",
"example1_coarse_cot_avg_20_frac_0.pdf",
"example1_coarse_cot_avg_20_frac_1.pdf",
"example1_coarse_cot_max_0_frac_0.pdf",
"example1_coarse_cot_max_10_frac_0.pdf",
"example1_coarse_cot_max_20_frac_0.pdf",
"example1_coarse_cot_min_0_frac_0.pdf",
"example1_coarse_cot_min_10_frac_0.pdf",
"example1_coarse_cot_min_20_frac_0.pdf",
"example1_coarse_mismatch_OPTfem_0.pdf",
"example1_coarse_mismatch_OPTfem_10.pdf",
"example1_coarse_mismatch_OPTfem_20.pdf",
"example1_coarse_mismatch_OPTxfem_0.pdf",
"example1_coarse_mismatch_OPTxfem_10.pdf",
"example1_coarse_mismatch_OPTxfem_20.pdf",
"example1_coarse_num_cells.pdf",
"example1_coarse_num_dof_F.pdf",
"example1_coarse_num_dof_T.pdf",
"example1_coarse_outflow_0.pdf",
"example1_coarse_outflow_10.pdf",
"example1_coarse_outflow_20.pdf",
"example1_coarse_outflow_star_19.pdf",
"example1_coarse_outflow_star_20.pdf",
"example1_fine_cot_avg_0_frac_0.pdf",
"example1_fine_cot_avg_0_frac_1.pdf",
"example1_fine_cot_avg_10_frac_0.pdf",
"example1_fine_cot_avg_10_frac_1.pdf",
"example1_fine_cot_avg_20_frac_0.pdf",
"example1_fine_cot_avg_20_frac_1.pdf",
"example1_fine_cot_max_0_frac_0.pdf",
"example1_fine_cot_max_10_frac_0.pdf",
"example1_fine_cot_max_20_frac_0.pdf",
"example1_fine_cot_min_0_frac_0.pdf",
"example1_fine_cot_min_10_frac_0.pdf",
"example1_fine_cot_min_20_frac_0.pdf",
"example1_fine_num_cells.pdf",
"example1_fine_num_dof_F.pdf",
"example1_fine_num_dof_T.pdf",
"example1_fine_outflow_0.pdf",
"example1_fine_outflow_10.pdf",
"example1_fine_outflow_20.pdf",
"label.pdf",]

for figure in figures:
    copyfile(folder_src + figure, folder_dist + figure)
