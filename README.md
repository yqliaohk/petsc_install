# petsc_install
This repo contains configure file(s) used for installing petsc

Copy the configure file into the folder `config/exmaples/`

Run the configure file from the root petsc directory, for example, by

```bash
./config/examples/arch-linux-gcc8-real-opt-mkl-ompi3.py

```
The modules and petsc version used with the configure file is specified in the file.
If you are using the same modules and petsc version, the configure file should work.
You can modify the options in the configure file as you want.
The link line for mkl blas and lapack can be found on the [intel website](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl/link-line-advisor.html).
