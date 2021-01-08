#!/sw/lsa/centos7/python-anaconda2/2019.03/bin/python
# --- Python 2.7 ---
'''
@File    :   arch-linux-gcc8-real-opt-mkl-ompi3.py
@Time    :   2020/12/15
@Author  :   Yingqian Liao
@Desc    :   Petsc configure example for GreatLakes cluster with mkl
'''
# =============================================================================================================
# Module list: python2.7-anaconda/2019.03   2) gcc/8.2.0   3) openmpi/3.1.6   4) cmake/3.13.2   5) mkl/2018.0.4
# =============================================================================================================

# ==============================================================================
# PETSc version: 3.11.4
# ==============================================================================

if __name__ == '__main__':
  import sys,os
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure_options = [
  '--with-shared-libraries',
  '--download-superlu_dist',
  '--download-parmetis=yes',
  '--download-metis=yes',
  '--with-fortran-bindings=1',
  '--with-debugging=0',
  '--with-scalar-type=real',
  '--PETSC_ARCH='+os.environ['PETSC_ARCH'],
  '--with-cxx-dialect=C++11',
  '--with-mpi-dir='+os.environ['MPI_HOME'],
  '--with-blas-lapack-lib= '+os.environ['MKLROOT']+'/lib/intel64/libmkl_scalapack_lp64.a -Wl,--start-group '+os.environ['MKLROOT']+'/lib/intel64/libmkl_intel_lp64.a '+os.environ['MKLROOT']+'/lib/intel64/libmkl_gnu_thread.a '+os.environ['MKLROOT']+'/lib/intel64/libmkl_core.a '+os.environ['MKLROOT']+'/lib/intel64/libmkl_blacs_openmpi_lp64.a -Wl,--end-group -lgomp -lpthread -lm -ldl', # This link can be found at mkl link advisor: https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl/link-line-advisor.html
  ]
  configure.petsc_configure(configure_options)




