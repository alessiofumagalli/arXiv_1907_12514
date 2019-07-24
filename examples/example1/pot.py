import matplotlib.pyplot as plt

import numpy as np
import os

# ------------------------------------------------------------------------------#

plt.rc("text", usetex=True)
plt.rc("font", family="serif")
plt.rc("font", size=15)


def plot_production(file_name, legend, title, **kwargs):

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
    frac_label = {0: "\\Omega_l", 1: "\\Omega_m", 2: "\\Omega_r"}

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

        ylabel = "$" + kwargs.get("ylabel", "\\theta") + "_{" + frac_label[frac_id] + "}$"

        plt_title = (
            title[0]
            + " on "
            + "$" + frac_label[frac_id] + "$"
            + " "
            + title[1]
            + " - "
            + " $C$"
            + str(title[2])
        )
        plt.title(plt_title)
        plt.xlabel("$t$")
        plt.ylabel(ylabel)
        plt.grid(True)
        if kwargs.get("do_legend", False):
            plt.legend()


# ------------------------------------------------------------------------------#

def plot_mismatch(file_name, title, num_traces, **kwargs):

    data = np.loadtxt(file_name, delimiter=",")
    fig = plt.figure(0)
    ax = fig.add_subplot(111)

    ylim = kwargs.get("ylim", None)
    if ylim is not None:
        ax.set_ylim(ylim)

    plt_title = (
        "mismatch on"
        + " "
        + title[0]
        + " for "
        + title[1]
        + " - "
        + " $C$"
        + str(title[2])
    )
    plt.title(plt_title)
    plt.xlabel("$t$")
    ylabel = "$\\delta \\Phi_{\\Gamma}$"
    plt.ylabel(ylabel)
    plt.grid(True)

    for trace_id in np.arange(num_traces):
        d = np.abs(data[:, trace_id + 1])
        label = "trace " + str(trace_id)
        plt.semilogy(data[:, 0], d, label=label)

    plt.legend()

# ------------------------------------------------------------------------------#


def plot_num_cells(data, legend, title):

    data = np.loadtxt(data, delimiter=",")
    data = np.atleast_2d(data)

    plt.figure(0)
    plt.plot(np.arange(data.shape[0]), data[:, -1], label=legend)
    plt.title(title)
    plt.xlabel("$C$")
    plt.ylabel("num. cells")
    plt.grid(True)
    #plt.legend()
    # useful to plot the legend as flat
    # ncol = 5 # number of methods
    # plt.legend(bbox_to_anchor=(1, -0.2), ncol=5)


# ------------------------------------------------------------------------------#

def plot_num_dofs(data, legend, title, **kwargs):

    data = np.loadtxt(data, delimiter=kwargs.get("delimiter", ","))
    if len(data.shape) > 1:
        data = np.sum(data, axis=1)

    plt.figure(0)
    plt.plot(np.arange(data.shape[0]), data, label=legend)
    plt.title(title)
    plt.xlabel("$C$")
    plt.ylabel("num. dof")
    plt.grid(True)
    #plt.legend()
    # useful to plot the legend as flat
    # ncol = 5 # number of methods
    # plt.legend(bbox_to_anchor=(1, -0.2), ncol=5)


# ------------------------------------------------------------------------------#

def plot_legend(legend, num_methods):

    plt.figure(0)
    plt.plot(np.zeros(1), label=legend)
    # useful to plot the legend as flat
    ncol = 5 # number of methods
    plt.legend(bbox_to_anchor=(1, -0.2), ncol=num_methods)

# ------------------------------------------------------------------------------#


def save_single(filename, folder, figure_id=0):

    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.figure(figure_id)
    plt.savefig(folder + "example1_" + filename + ".pdf", bbox_inches="tight")
    plt.gcf().clear()


# ------------------------------------------------------------------------------#


def save_multiple(filename, num_frac, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    for frac_id in np.arange(num_frac):
        plt.figure(frac_id)
        name = filename + "_frac_" + str(frac_id)
        plt.savefig(folder + "example1_" + name + ".pdf", bbox_inches="tight")
        plt.gcf().clear()


# ------------------------------------------------------------------------------#

def save_multiple_trace(filename, num_traces, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.figure(0)
    plt.savefig(folder + "example1_" + filename + ".pdf", bbox_inches="tight")
    plt.gcf().clear()

# ------------------------------------------------------------------------------#

def save_label(filename, folder, figure_id=0):

    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.figure(figure_id)
    plt.savefig(folder + filename + ".pdf", bbox_inches="tight")
    plt.gcf().clear()


# ------------------------------------------------------------------------------#


def main():

    num_simul = 21
    num_frac = 3
    num_traces = 2

    master_folder = "./"

    methods_stefano_1 = ["OPTxfem", "OPTfem"]
    methods_stefano_2 = ["GCmfem"]
    methods_stefano_3 = ["OPTxfemG", "OPTfemG"]

    methods_alessio = ["MVEM_UPWIND", "Tpfa_UPWIND", "RT0_UPWIND"]

    style = lambda s: "$\\textsc{"+s+"}$"
    label = {"OPTxfem": style("XFEMSUPG"), "OPTfem": style("FEMSUPG"), "GCmfem": style("MFEMSUPG"),
             "OPTxfemG": style("XFEMSUPG*"), "OPTfemG": style("FEMSUPG*"),
             "MVEM_UPWIND": style("MVEMUP"), "Tpfa_UPWIND": style("TPFAUP"),
             "RT0_UPWIND": style("MFEMUP")}

    method_reference = "GCmfem"
    reference = {"grid_0": 10, "grid_1": 5, "grid_2": 3.5}

    grids = {
        "grid_0": ("1k", "220", "1", "0.005"),
        "grid_1": ("3k", "650", "3", "0.0015"),
        "grid_2": ("10k", "2100", "10", "0.00045"),
    }
    grids_label = {"grid_0": "coarse", "grid_1": "medium", "grid_2": "fine"}

    folder_in = master_folder
    folder_out = folder_in + "img/"

    for grid_name, grid in grids.items():
        grid_label = grids_label[grid_name]
        for simul in np.arange(num_simul):

            title = ["averaged $\\theta$", grid_label, simul]
            ylabel = "\\langle {\\theta} \\rangle"

            # Reference
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_Cmean_"
                + str(simul + 1)
                + "_big"
                + ".csv"
            )
            plot_multiple(data, None, title, num_frac, reference=reference[grid_name], ylabel=ylabel)

            # Alessio
            for method in methods_alessio:
                data = (
                    folder_in
                    + method
                    + "/"
                    + "Cmean_"
                    + str(simul + 1)
                    + "_"
                    + grid[0]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # Stefano
            for method in methods_stefano_1:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_Cmean_"
                    + str(simul + 1)
                    + "_"
                    + grid[1]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            for method in methods_stefano_2:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_Cmean_"
                    + str(simul + 1)
                    + "_"
                    + grid[2]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # save
            name = grid_label + "_cot_avg_" + str(simul)
            save_multiple(name, num_frac, folder_out)

            ###########

            title = ["min $\\theta$", grid_label, simul]
            ylabel = "\\min {\\theta}"

            # Reference
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_Cmin_"
                + str(simul + 1)
                + "_big"
                + ".csv"
            )
            plot_multiple(data, None, title, num_frac, reference=reference[grid_name], ylabel=ylabel)

            # Alessio
            for method in methods_alessio:
                data = (
                    folder_in
                    + method
                    + "/"
                    + "Cmin_"
                    + str(simul + 1)
                    + "_"
                    + grid[0]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # Stefano
            for method in methods_stefano_1:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_Cmin_"
                    + str(simul + 1)
                    + "_"
                    + grid[1]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # Stefano
            for method in methods_stefano_2:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_Cmin_"
                    + str(simul + 1)
                    + "_"
                    + grid[2]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # save
            name = grid_label + "_cot_min_" + str(simul)
            save_multiple(name, num_frac, folder_out)

            ###########

            title = ["max $\\theta$", grid_label, simul]
            ylabel = "\\max {\\theta}"

            # Reference
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_Cmax_"
                + str(simul + 1)
                + "_big"
                + ".csv"
            )
            plot_multiple(data, None, title, num_frac, reference=reference[grid_name], ylabel=ylabel)

            # Alessio
            for method in methods_alessio:
                data = (
                    folder_in
                    + method
                    + "/"
                    + "Cmax_"
                    + str(simul + 1)
                    + "_"
                    + grid[0]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # Stefano
            for method in methods_stefano_1:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_Cmax_"
                    + str(simul + 1)
                    + "_"
                    + grid[1]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            for method in methods_stefano_2:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_Cmax_"
                    + str(simul + 1)
                    + "_"
                    + grid[2]
                    + ".csv"
                )
                plot_multiple(data, label[method], title, num_frac, ylabel=ylabel)

            # save
            name = grid_label + "_cot_max_" + str(simul)
            save_multiple(name, num_frac, folder_out)

           ###########

            title = grid_label + " - $C$" + str(simul)
            ylabel = "\\langle {\\theta} \\rangle_{\\rm outflow}"

            # Reference
            data = (
                folder_in
                + method_reference
                + "/"
                + method_reference
                + "_production_"
                + str(simul + 1)
                + "_big"
                + ".csv"
            )
            plot_production(data, None, title, reference=reference[grid_name], ylabel=ylabel)

            # Alessio
            for method in methods_alessio:
                data = (
                    folder_in
                    + method
                    + "/"
                    + "production_"
                    + str(simul + 1)
                    + "_"
                    + grid[0]
                    + ".csv"
                )
                plot_production(data, label[method], title, ylabel=ylabel)

            # Stefano
            for method in methods_stefano_1:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_production_"
                    + str(simul + 1)
                    + "_"
                    + grid[1]
                    + ".csv"
                )
                plot_production(data, label[method], title, ylabel=ylabel)

            for method in methods_stefano_2:
                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_production_"
                    + str(simul + 1)
                    + "_"
                    + grid[2]
                    + ".csv"
                )
                plot_production(data, label[method], title, ylabel=ylabel)

            # save
            name = grid_label + "_outflow_" + str(simul)
            save_single(name, folder_out)

            ########

            if grid_name == "grid_0":

                title = grid_label + " - $C$" + str(simul)
                ylabel = "\\langle {\\theta} \\rangle_{\\rm outflow}"

                # Reference
                data = (
                    folder_in
                    + method_reference
                    + "/"
                    + method_reference
                    + "_production_"
                    + str(simul + 1)
                    + "_big"
                    + ".csv"
                )
                plot_production(data, None, title, reference=reference[grid_name], ylabel=ylabel)

                # Alessio
                for method in methods_alessio:
                    data = (
                        folder_in
                        + method
                        + "/"
                        + "production_"
                        + str(simul + 1)
                        + "_"
                        + grid[0]
                        + ".csv"
                    )
                    plot_production(data, None, title, ylabel=ylabel, alpha=0.5, color="gray")

                # Stefano
                for method in methods_stefano_1:
                    data = (
                        folder_in
                        + method
                        + "/"
                        + method
                        + "_production_"
                        + str(simul + 1)
                        + "_"
                        + grid[1]
                        + ".csv"
                    )
                    plot_production(data, None, title, ylabel=ylabel, alpha=0.5, color="gray")

                for method in methods_stefano_2:
                    data = (
                        folder_in
                        + method
                        + "/"
                        + method
                        + "_production_"
                        + str(simul + 1)
                        + "_"
                        + grid[2]
                        + ".csv"
                    )
                    plot_production(data, None, title, ylabel=ylabel, alpha=0.5, color="gray")

                for method in methods_stefano_3:
                    data = (
                        folder_in
                        + method
                        + "/"
                        + method
                        + "_production_"
                        + str(simul + 1)
                        + "_"
                        + grid[2]
                        + ".csv"
                    )
                    if method == "OPTxfemG":
                        color = "r"
                    else:
                        color = "b"
                    plot_production(data, label[method], title, ylabel=ylabel, color=color, do_legend=True)

                # save
                name = grid_label + "_outflow_star_" + str(simul)
                save_single(name, folder_out)


            ########


            # Stefano
            for method in methods_stefano_1:
                title = [grid_label, label[method], simul]

                data = (
                    folder_in
                    + method
                    + "/"
                    + method
                    + "_mismatch_"
                    + str(simul + 1)
                    + "_"
                    + grid[1]
                    + ".csv"
                )
                plot_mismatch(data, title, num_traces)

                # save
                name = grid_label + "_mismatch_" + method + "_" + str(simul)
                save_multiple_trace(name, num_traces, folder_out)

            ########

        title = "number of cells - " + grid_label
        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "num_cells_" + grid[0] + ".csv"
            plot_num_cells(data, label[method], title)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + "num_cells_" + grid[1] + ".csv"
            plot_num_cells(data, label[method], title)

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_cells_" + grid[2] + ".csv"
            plot_num_cells(data, label[method], title)

        name = grid_label + "_num_cells"
        save_single(name, folder_out)

        ########

        title = "number of dof flow - " + grid_label
        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "numdofF_" + grid[0] + ".csv"
            plot_num_dofs(data, label[method], title)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + method + "_numdofF_" + grid[1] + ".csv"
            plot_num_dofs(data, label[method], title, delimiter=" ")

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_numdofF_" + grid[2] + ".csv"
            plot_num_dofs(data, label[method], title, delimiter=" ")

        name = grid_label + "_num_dof_F"
        save_single(name, folder_out)

        ########

        title = "number of dof transport - " + grid_label
        # Alessio
        for method in methods_alessio:
            data = folder_in + method + "/" + "numdofT_" + grid[0] + ".csv"
            plot_num_dofs(data, label[method], title)

        # Stefano
        for method in methods_stefano_1:
            data = folder_in + method + "/" + method + "_numdofT_" + grid[1] + ".csv"
            plot_num_dofs(data, label[method], title, delimiter=" ")

        for method in methods_stefano_2:
            data = folder_in + method + "/" + method + "_numdofT_" + grid[2] + ".csv"
            plot_num_dofs(data, label[method], title, delimiter=" ")

        name = grid_label + "_num_dof_T"
        save_single(name, folder_out)

        ########

    methods = methods_alessio + methods_stefano_1 + methods_stefano_2
    num_methods = len(methods)

    for method in methods:
        plot_legend(label[method], num_methods)

    name = "label"
    save_label(name, folder_out)
    full_name = folder_out + name + ".pdf"
    os.system("pdfcrop --margins '0 -300 0 0' " + full_name + " " + full_name)
    os.system("pdfcrop " + full_name + " " + full_name)

# ------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
