# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:10:09 2024

@author: rezaf
"""

import unittest
import os
from assessment3_part1 import pdfmerge, pdfrotate, pdfencrypt, pdfdecrypt
from pypdf import PdfReader


class Testpdffunctions(unittest.TestCase):
    
    def setUp(self):
        self.pdfs = ['reza1.pdf', 'reza2.pdf']
        self.combined_output = 'combined_reza.pdf'
        self.rotated_output = 'rotated_reza1.pdf'
        self.encrypted_output = 'encrypted_reza.pdf'
        self.decrypted_output = 'decrypted_reza.pdf'
        self.password = "P@ssw0rd"
    
    def tearDown(self):
        # Clean up generated test files
        for file in [self.combined_output, self.rotated_output, self.encrypted_output, self.decrypted_output]:
            if os.path.exists(file):
                os.remove(file)    
                
    def test_pdfmerge(self):
        pdfmerge(self.pdfs, self.combined_output)      
        self.assertTrue(os.path.exists(self.combined_output))
        
    def test_pdfrotate(self):
        pdfrotate(self.pdfs[0], self.rotated_output, 270)
        rotate = PdfReader(self.rotated_output)
        self.assertTrue(os.path.exists(self.rotated_output))
        self.assertEqual(rotate.pages[0].rotation, 270)
        
    def test_pdfencrypt(self):
        pdfencrypt(self.pdfs[0], self.encrypted_output, self.password)
        read = PdfReader(self.encrypted_output)
        self.assertTrue(os.path.exists(self.encrypted_output))
        self.assertTrue(read.is_encrypted)
    
    def test_pdfdecrypt(self):
    # Encrypt the file first to ensure encrypted_output exists
        pdfencrypt(self.pdfs[0], self.encrypted_output, self.password)
        pdfdecrypt(self.encrypted_output, self.decrypted_output, self.password)
        read = PdfReader(self.decrypted_output)
        self.assertTrue(os.path.exists(self.decrypted_output))
        self.assertFalse(read.is_encrypted)
        
        
        
if __name__ == "__main__":
    unittest.main()         
        
        
        
        