import matplotlib.pyplot as plt
import numpy as np
import os

# ------------------------------------------------------------------------------#

plt.rc("text", usetex=True)
plt.rc("font", family="serif")
plt.rc("font", size=15)


def plot_production(file_name, legend, title, **kwargs):

    data = np.loadtxt(file_name, delimiter=",")
    fct = kwargs.get("fct", lambda x: x)

    plt.figure(0)
    plt.plot(data[:, 0], fct(data[:, 1]), label=legend)
    plt.title("averaged $\\theta$ at outflow on " + title)
    plt.xlabel("$t$")
    ylabel = "$" + kwargs.get("ylabel", "\\theta") + "$"
    plt.ylabel(ylabel)
    plt.grid(True)
    if kwargs.get("do_legend", False):
        plt.legend()


# ------------------------------------------------------------------------------#


def plot_multiple(file_name, legend, title, num_frac, **kwargs):

    data = np.loadtxt(file_name, delimiter=",")

    for frac_id in np.arange(num_frac):
        plt.figure(frac_id)
        plt.plot(data[:, 0], data[:, frac_id + 1], label=legend)

        ylabel = "$" + kwargs.get("ylabel", "\\theta") + "_{\\Omega_{" + str(frac_id) + "}}$"
        plt_title = (
            title[0] + " on " + "$\\Omega_{" + str(frac_id) + "}$" + " " + title[1]
        )
        plt.title(plt_title)
        plt.xlabel("$t$")
        plt.ylabel(ylabel)
        plt.grid(True)
        if kwargs.get("do_legend", False):
            plt.legend()


# ------------------------------------------------------------------------------#


def save_single(filename, folder, figure_id=0):

    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.figure(figure_id)
    plt.savefig(folder + "example3_" + filename + ".pdf", bbox_inches="tight")
    plt.gcf().clear()


# ------------------------------------------------------------------------------#


def save_multiple(filename, num_frac, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    for frac_id in np.arange(num_frac):
        plt.figure(frac_id)
        name = filename + "_frac_" + str(frac_id)
        plt.savefig(folder + "example3_" + name + ".pdf", bbox_inches="tight")
        plt.gcf().clear()


# ------------------------------------------------------------------------------#


def main():

    num_frac = 89-7

    master_folder = "./"

    methods_stefano = ["OPTfem", "OPTxfem", "GCmfem"]
    methods_alessio = ["MVEM_UPWIND", "Tpfa_UPWIND", "RT0_UPWIND"]

    cases = {"case_0": ("different", "different", "0.005"), "case_1": ("same", "same", "0.001")}
    cases_label_file_name = {"case_0": "different", "case_1": "same"}
    cases_label = {"case_0": "\\textit{case 1}", "case_1": "\\textit{case 2}"}

    style = lambda s: "$\\textsc{"+s+"}$"
    label = {"OPTxfem": style("XFEMSUPG"), "OPTfem": style("FEMSUPG"), "GCmfem": style("MFEMSUPG"),
             "OPTxfemG": style("XFEMSUPG*"), "OPTfemG": style("FEMSUPG*"),
             "MVEM_UPWIND": style("MVEMUP"), "Tpfa_UPWIND": style("TPFAUP"),
             "RT0_UPWIND": style("MFEMUP")}


    for case_name, case in cases.items():
        case_label = cases_label[case_name]

        folder_in = master_folder
        folder_out = folder_in + "img/"

        title = ["averaged $\\theta$", "on " + case_label]
        ylabel = "\\langle {\\theta} \\rangle"
        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "Cmean_" + case[0] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # Stefano
        for method in methods_stefano:
            data = folder_in + method + "/" + method + "_Cmean_" + case[1] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # save
        name = cases_label_file_name[case_name] + "_cot_avg"
        save_multiple(name, num_frac, folder_out)

        ###########

        title = ["min $\\theta$", "on " + case_label]
        ylabel = "\\min {\\theta}"
        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "Cmin_" + case[0] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # Stefano
        for method in methods_stefano:
            data = folder_in + method + "/" + method + "_Cmin_" + case[1] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # save
        name = cases_label_file_name[case_name] + "_cot_min"
        save_multiple(name, num_frac, folder_out)

        ###########

        title = ["max $\\theta$", "on " + case_label]
        ylabel = "\\max {\\theta}"

        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "Cmax_" + case[0] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # Stefano
        for method in methods_stefano:
            data = folder_in + method + "/" + method + "_Cmax_" + case[1] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # save
        name = cases_label_file_name[case_name] + "_cot_max"
        save_multiple(name, num_frac, folder_out)

        ###########

        title = case_label
        ylabel = "\\langle {\\theta} \\rangle_{\\rm outflow}"

        # Alessio
        if case_name == "case_0":
            fct = lambda x: x / 381. + 273.15
        elif case_name == "case_1":
            fct = lambda x: x / 291.58 + 273.15
        else:
            ssss

        for method in methods_alessio:
            data = folder_in + method + "/" + "production_" + case[0] + ".csv"
            plot_production(data, label[method], title, ylabel=ylabel, fct=fct)

        # Stefano
        length = 1.0
        for method in methods_stefano:
            data = folder_in + method + "/" + method + "_production_" + case[1] + ".csv"
            plot_production(data, label[method], title, ylabel=ylabel)

        # save
        name = cases_label_file_name[case_name] + "_outflow"
        save_single(name, folder_out)


# ------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
