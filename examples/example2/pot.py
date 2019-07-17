import matplotlib.pyplot as plt
import numpy as np
import os

# ------------------------------------------------------------------------------#

plt.rc("text", usetex=True)
plt.rc("font", family="serif")
plt.rc("font", size=15)


def plot_single(file_name, legend, title, **kwargs):

    data = np.loadtxt(file_name, delimiter=",")
    reference = kwargs.get("reference", None)

    fig = plt.figure(0)
    ax = fig.add_subplot(111)

    # if the data is a reference
    if reference:
        data_p = data[:, 1] + data[:, 1] * reference / 100
        plt.plot(data[:, 0], data_p, label=legend, linestyle="--", color="gray")
        text = "ref + " + str(reference) + "\%"
        pos = (np.median(data[:, 0]), np.median(data_p))
        pos_t = (pos[0], pos[1]+5*pos[1]/100)
        ax.annotate(text, xy=pos, xytext=pos_t)

        data_m = data[:, 1] - data[:, 1] * reference / 100
        plt.plot(data[:, 0], data_m, label=legend, linestyle="--", color="gray")
        text = "ref - " + str(reference) + "\%"
        pos = (np.median(data[:, 0]), np.median(data_m))
        pos_t = (pos[0], pos[1]-5*pos[1]/100)
        ax.annotate(text, xy=pos, xytext=pos_t)

    else:
        color = kwargs.get("color", None)
        if color is None:
            plt.plot(data[:, 0], data[:, 1], label=legend, alpha=kwargs.get("alpha", 1))
        else:
            plt.plot(data[:, 0], data[:, 1], label=legend, alpha=kwargs.get("alpha", 1), color=color)

    plt.title(title)
    plt.xlabel("$t$")
    ylabel = "$" + kwargs.get("ylabel", "\\theta") + "$"
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()

# ------------------------------------------------------------------------------#

def plot_multiple(file_name, legend, title, num_frac, **kwargs):

    data = np.loadtxt(file_name, delimiter=",")
    reference = kwargs.get("reference", None)

    for frac_id in np.arange(num_frac):
        fig = plt.figure(frac_id)
        ax = fig.add_subplot(111)

        # if the data is a reference
        if reference:
            data_p = data[:, frac_id + 1] + data[:, frac_id + 1] * reference / 100
            plt.plot(data[:, 0], data_p, label=legend, linestyle="--", color="gray")
            text = "ref + " + str(reference) + "\%"
            pos = (np.median(data[:, 0]), np.median(data_p))
            pos_t = (pos[0], pos[1]+5*pos[1]/100)
            ax.annotate(text, xy=pos, xytext=pos_t)

            data_m = data[:, frac_id + 1] - data[:, frac_id + 1] * reference / 100
            plt.plot(data[:, 0], data_m, label=legend, linestyle="--", color="gray")
            text = "ref - " + str(reference) + "\%"
            pos = (np.median(data[:, 0]), np.median(data_m))
            pos_t = (pos[0], pos[1]-5*pos[1]/100)
            ax.annotate(text, xy=pos, xytext=pos_t)

        else:
            plt.plot(data[:, 0], data[:, frac_id + 1], label=legend)

        ylabel = "$" + kwargs.get("ylabel", "\\theta") + "_{\\Omega_{" + str(frac_id) + "}}$"

        plt_title = (
            title[0] + " on " + "$\\Omega_{" + str(frac_id) + "}$" + " " + title[1]
        )
        plt.title(plt_title)
        plt.xlabel("$t$")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.legend()


# ------------------------------------------------------------------------------#

def plot_mismatch(file_name, title, num_traces, **kwargs):

    data = np.loadtxt(file_name, delimiter=",")
    fig = plt.figure(0)
    ax = fig.add_subplot(111)

    plt_title = (
        title[0]
        + " "
        + title[1]
        + " for "
        + title[2]
    )
    plt.title(plt_title)
    plt.xlabel("$t$")
    ylabel = "$\\delta \\Phi_{\\Gamma, i}$"
    plt.ylabel(ylabel)
    plt.grid(True)

    for trace_id in np.arange(num_traces):
        d = np.abs(data[:, trace_id + 1])
        label = "$\\delta \\Phi_{\\Gamma, " + str(trace_id) + "}$"
        #plt.semilogy(data[:, 0], d, label=label)
        plt.semilogy(data[:, 0], d)

    #plt.legend()

# ------------------------------------------------------------------------------#


def save_single(filename, folder, figure_id=0):

    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.figure(figure_id)
    plt.savefig(folder + filename + ".pdf", bbox_inches="tight")
    plt.gcf().clear()


# ------------------------------------------------------------------------------#


def save_multiple(filename, num_frac, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    for frac_id in np.arange(num_frac):
        plt.figure(frac_id)
        name = filename + "_frac_" + str(frac_id)
        plt.savefig(folder + name + ".pdf", bbox_inches="tight")
        plt.gcf().clear()


# ------------------------------------------------------------------------------#

def save_multiple_trace(filename, num_traces, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.figure(0)
    plt.savefig(folder + filename + ".pdf", bbox_inches="tight")
    plt.gcf().clear()


# ------------------------------------------------------------------------------#


def main():

    num_frac = 10
    num_traces = 14

    master_folder = "/home/elle/Dropbox/Work/PresentazioniArticoli/2019/Articles/dfn_transport/tipetut++/Results/example2/"

    methods_stefano_1 = ["OPTxfem", "OPTfem"]
    methods_stefano_2 = ["GCmfem"]
    methods_alessio = ["MVEM_UPWIND", "Tpfa_UPWIND", "RT0_UPWIND"]

    style = lambda s: "$\\textsc{"+s+"}$"
    label = {"OPTxfem": style("XFEMSUPG"), "OPTfem": style("FEMSUPG"), "GCmfem": style("MFEMSUPG"),
             "OPTxfemG": style("XFEMSUPG*"), "OPTfemG": style("FEMSUPG*"),
             "MVEM_UPWIND": style("MVEMUP"), "Tpfa_UPWIND": style("TPFAUP"),
             "RT0_UPWIND": style("MFEMUP")}

    if_reference = True
    method_reference = "GCmfem"
    reference = {"grid_0": 10, "grid_1": 5}

    grids = {
        "grid_0": ("3k", "200", "3", "9e-05"),
        "grid_1": ("40k", "2600", "40", "0.0015"),
    }
    grids_label = {"grid_0": "coarse", "grid_1": "fine"}

    for grid_name, grid in grids.items():
        grid_label = grids_label[grid_name]

        folder_in = master_folder
        folder_out = folder_in + "img/"

        title = ["avg $\\theta$", grid_label]
        ylabel = "\\overline{\\theta}"

        if if_reference:
            # Reference
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_Cmean_big"
                + ".csv"
            )
            plot_multiple(data, None, title, num_frac, reference=reference[grid_name], ylabel=ylabel)

        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "Cmean_" + grid[0] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + method + "_Cmean_" + grid[1] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_Cmean_" + grid[2] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # save
        name = grid_label + "_cot_avg"
        save_multiple(name, num_frac, folder_out)

        ###########

        title = ["min $\\theta$", grid_label]
        ylabel = "\\min {\\theta}"

        # Reference
        if if_reference:
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_Cmin_big"
                + ".csv"
            )
            plot_multiple(data, None, title, num_frac, reference=reference[grid_name], ylabel=ylabel)

        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "Cmin_" + grid[0] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + method + "_Cmin_" + grid[1] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_Cmin_" + grid[2] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # save
        name = grid_label + "_cot_min"
        save_multiple(name, num_frac, folder_out)

        ###########

        title = ["max $\\theta$", grid_label]
        ylabel = "\\max {\\theta}"

        # Reference
        if if_reference:
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_Cmax_big"
                + ".csv"
            )
            plot_multiple(data, None, title, num_frac, reference=reference[grid_name], ylabel=ylabel)

        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "Cmax_" + grid[0] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + method + "_Cmax_" + grid[1] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_Cmax_" + grid[2] + ".csv"
            plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

        # save
        name = grid_label + "_cot_max"
        save_multiple(name, num_frac, folder_out)

        ###########

        title = "production on " + grid_label
        ylabel = "\\Pi^{\\rm outflow}"

        if if_reference:
            # Reference
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_production_big"
                + ".csv"
            )
            plot_single(data, None, title, reference=reference[grid_name], ylabel=ylabel)

        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "production_" + grid[0] + ".csv"
            plot_single(data, label[method], title, ylabel=ylabel)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + method + "_production_" + grid[1] + ".csv"
            plot_single(data, label[method], title, ylabel=ylabel)

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_production_" + grid[2] + ".csv"
            plot_single(data, label[method], title, ylabel=ylabel)

        # save
        name = grid_label + "_outflow"
        save_single(name, folder_out)

        ###########

        title = ["mismatch", grid_label, label[method]]

        # Stefano
        for method in methods_stefano_1:
            data = (
                folder_in
                + method
                + "/"
                + method
                + "_mismatch_"
                + grid[1]
                + ".csv"
            )
            plot_mismatch(data, title, num_traces)

            # save
            name = grid_label + "_mismatch_" + method
            save_multiple_trace(name, num_traces, folder_out)

        ########

# ------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
