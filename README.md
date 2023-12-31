# BME4931 Problem Sets

Welcome to the BME4931 Problem Sets repository! This repository is dedicated to organizing and providing resources for the in-person problem sets BME4931: Medical AI. The content is structured into different directories to facilitate easy navigation and access to the materials. During the course, I will be pushing new Problem Sets weekly. My goal is to have the problem set finished for each week by Thursday morning, but please realize that I make these problem sets from scratch and sometimes it does take longer than expected. 

## License

This repository is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) or later. Please refer to the [LICENSE](LICENSE) file for more details.

## Directory Structure

### Homework 3

The `Homework 3` directory contains all the files necessary for the completion of Homework 3.

### Modules:

Modules are categorized by numbers ranging from 02 to 13*. Each module directory contains a series of subdirectories corresponding to the problem sets and their solutions. The first two modules (Module 02 and Module 03) primarily consist of tutorials rather than problem set/solution combinations. Occasionally, there may also be a `data` folder within these directories, containing data required for the problem sets\*\*.

- **Module 02: Python Primer**: Tutorial content***
- **Module 03: Biomedical Data**: Tutorial content***
- **Module 04: Data Wrangling**
- **Module 05: Machine Learning Basics**
- ...
- **Module 13: Dimensionality Reduction**

\* Module 11 does not exist as it was an in-person lecture on transformers

\** All data necessary to run these files can be found in the data directory with the exception of the data for the LSTM found in Module 10. Currently this must be downloaded from the Course Canvas page as it is too large for GitHub.

\*** These modules only contain tutorial content - as the course was in its infancy we planned to do weekly tutorials. Based on feedback, we switched to weekly problem sets instead. 

### bonus

The `bonus` directory contains more in-depth code and covers complicated topics touched on in class but not given their own module. This section provides additional challenges and explores advanced concepts for those seeking to delve deeper into the subject matter.

## Getting Started

To get started, navigate to the relevant module or homework directory and explore the associated Jupyter notebooks. Each problem set and solution is organized within its corresponding module for easy access. To run the notebooks yourself, make changes, or just play around I find it easiest to clone the repository to a directory of your choice and then run `$ jupyter-notebook` in that directory (which of course requires Jupyter notebook).

## Data

All data present in these files/notebooks is open source and/or licensed appropritely for the class. Most datasets are external and loaded in with appropriate credit and information describing them in the problem sets. In the cases where the dataset is not credited, the data has been generated by me for the purposes of the Problem Sets (not real data). 

## Roadmap

I plan to make the following (non-exhaustive) changes/updates to the repository as time permits/as it makes sense for the class (in no particular order)
  - Convert Module 2 and Module 3 to Problem Sets instead of tutorials
  - Add to the bonus directory
    - LSTM preprocessing scripts for the data in Module 10
    - Transformer example notebook
  - Create a Problem Set for Module 11
  - Create a requirements file
  - Modify the data in Module 10 so that it can be added to GitHub

## Contributions

If you find errors or have improvements to suggest for existing problem sets, feel free to open an issue or submit a pull request. However, due to the nature of the course, the module content is more-or-less set in stone. If you would like to add content outside the scope of the modules, you *must* do so in the bonus directory. PRs that attempt to add new modules will be denied. 

There's always more out there to learn, especially in this field! Your contributions are highly appreciated! 

\- J 
