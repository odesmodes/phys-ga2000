import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data


numG = 10
for i in range(0,numG):
    plt.plot(logwave,flux[i],label="Galaxy {index}".format(index = i))

plt.ylabel('flux (10e-17 erg / (s cm^2 A))')
plt.xlabel('log lambda (A)')
plt.legend()

plt.savefig('10 galaxies')
plt.close()

normalizations = np.trapz(flux,logwave, axis=1)
normalized_flux = flux/normalizations[:,np.newaxis]

means=np.mean(normalized_flux,axis=0)
residuals=normalized_flux - means

for i in range(0,numG):
    plt.plot(logwave,residuals[i],label="Galaxy {index}".format(index = i))

plt.ylabel('flux (10e-17 erg / (s cm^2 A))')
plt.xlabel('log lambda (A)')
plt.legend()
plt.savefig('normalized and subtracted')
plt.close()

cov_mat = np.cov(residuals.T)

eigenvalues, eigenvectors = np.linalg.eig(cov_mat)

for i in range(5):
    plt.plot(eigenvectors[:,i], label="Eigenvector {index}".format(index=i))

plt.xlabel("Index")
plt.ylabel("Eigenvector Value")
plt.legend()
plt.savefig('Eigenvector.png')
plt.close()

U, S, Vt = np.linalg.svd(residuals, full_matrices=False)
for i in range(5):
    plt.plot(logwave, Vt[i], label="Eigenvector {index}".format(index=i))

plt.xlabel("Wavelength (A)")
plt.ylabel("Eigenvector Value")
plt.legend()
plt.savefig('Eigenvector SVD.png')
plt.close()

#some of these may look "flipped", but the eigenvectors still represent the same things

#keeping 5 coeffs
Nc = 5
coeffs = np.dot(residuals, eigenvectors)

approx_spectra = np.dot(coeffs[:,:Nc], eigenvectors[:,:Nc].T) + means

for i in range(numG):
    plt.plot(logwave, approx_spectra[i], label="Approximate spectra {index}".format(index=i))
plt.ylabel('flux (10e-17 erg / (s cm^2 A))')
plt.xlabel('log lambda (A)')
plt.legend()
plt.savefig('Approximate Spectra')
plt.close()

c0 = coeffs[:,0]
c1 = coeffs[:,1]
c2 = coeffs[:,2]

plt.scatter(c0,c1)
plt.savefig('c0 vs c1.png')
plt.xlabel('c0')
plt.ylabel('c1')
plt.close()

plt.scatter(c0,c2)
plt.savefig('c0 vs c2.png')
plt.xlabel('c0')
plt.ylabel('c2')
plt.close()

rms_reses = []
for Nc in range(1,21):
    approx_flux = np.dot(coeffs[:,:Nc],eigenvectors[:,:Nc].T) + means
    residual = np.sum((flux-approx_flux)**2, axis=1)
    rms_reses.append(np.mean(residual))

plt.plot(range(1,21), rms_reses, marker='.')
plt.xlabel("Nc")
plt.ylabel("RMS residuals")
plt.savefig('RMS vs Nc.png')
plt.close()
