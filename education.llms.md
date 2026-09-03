# Positron for Education

Bring Positron to your classroom with a free education license.

## A true multi-language IDE for data science for all

With Positron, students get access to a robust data science IDE with features designed to support learning and productivity, including:

- A professional IDE tailored for data science
- Rich Python and R support
- A built-in **Data Explorer** and **Variables** pane
- An integrated **Help** pane, debugger, and version control
- Optional AI assistance for pair programming and debugging

Explore the full list of [Positron features](features.llms.md).

## How can I use Positron in an educational setting?

- Under the [Positron Elastic license](licensing.llms.md), individuals may install and use Positron Desktop for any purpose.
- Qualified academic institutions can host Positron as a service in the following ways. All of them require a [license](licensing.llms.md#positron-education-license-rider).
  - [Positron Server for Jupyter](https://posit-dev.github.io/jupyter-positron-server/)
  - [Posit Workbench for Education](https://posit.co/pricing/academic#we-help-educators)

> **NOTE:**
>
> Reach out via a discussion in our [GitHub repository](https://github.com/posit-dev/positron/discussions).

## Eligibility for education licenses

Academic institutions can use Positron Server or Positron on Workbench for teaching with a free education license. Full eligibility details are in the Positron [Academic License Rider](licensing.llms.md#positron-education-license-rider).

Free licenses for academic research are also available on a case-by-case basis; see the [FAQ below](#can-i-get-a-free-license-for-academic-research) for details.

## Applying for an education license

1.  **Check eligibility.** Review the [Positron Education License Rider](licensing.llms.md#positron-education-license-rider) to confirm qualification for an education license.

2.  **Request a license.** Send an email to <academic-licenses@posit.co> to get a free education license key.

3.  **Install instructions.** Follow the instructions for your installation method to get Positron up and running. For example, for installing Positron on JupyterHub:

    - See the [`jupyter-positron-server` documentation](https://posit-dev.github.io/jupyter-positron-server/) to complete setup.
    - Watch the [installation walkthrough](https://www.loom.com/share/9a8c760a4d4e45b2ac78d62ba3e1d0b3) for a step-by-step guide.

## Frequently asked questions

#### How much does an education license cost?

Education licenses are free for qualified academic institutions.

#### Does an education license for teaching cover both Positron Server and Positron on Workbench?

Yes, with an education license you can choose multiple distribution options, including Positron Server and Positron on Workbench.

#### Can I get a free license for academic research?

Possibly. We grant free licenses for academic research on a case-by-case basis, typically for research conducted at degree-granting academic institutions. These licenses are not intended for all research settings; for example, research and development at corporate research labs or similar large-scale research organizations generally requires a paid [Posit Workbench](https://posit.co/pricing/academic#we-help-educators) license. In that scenario, Posit does still provide a [research discount](https://posit.co/pricing/academic) for Posit Workbench where appropriate.

Individuals can also use Positron Desktop for any purpose, including research, under the [Positron Elastic license](licensing.llms.md). To inquire about a free academic research license, email <academic-licenses@posit.co> with a brief description of your research and institution.

#### Does the license expire at the end of the semester?

The license lasts for 12 months from the desired start date you indicate when applying. Please note, we only process licenses within two months before the start of a semester.

#### Can I disable specific extensions for all students on JupyterHub?

An admin can configure settings in the machine-level settings file, available at a path like `/home/jupyter-admin/.positron-server/data/Machine/settings.json`. You can use the [`extensions.allowed` setting](https://code.visualstudio.com/docs/enterprise/extensions#_configure-allowed-extensions) to approve or deny extensions for all users on your JupyterHub server.

#### How do I upgrade Positron Server to the latest version?

Install the latest version of Positron to the same location.

#### Can I pre-configure a default environment (specific packages, files, settings) so all students start from the same place?

Positron can locate Python environments as well as any files on a user’s JupyterHub instance, so packages and files in shared locations are automatically available. An admin can configure settings in the machine-level settings file, available at a path like `/home/jupyter-admin/.positron-server/data/Machine/settings.json`.

#### Can I use Positron Server alongside Jupyter Notebooks at the same time?

Yes, Positron has a native Jupyter editor your students can work with. You can also have students open two tabs, one with Positron and another with JupyterLab.
