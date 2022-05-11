# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bSIYVmkOtFmEVawUJ52HXwwm3uFLseo-
"""

!pip3 install torch==1.8.2+cu102 torchvision==0.9.2+cu102 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

!pip3 install transformers

!pip3 install sentencepiece

from transformers import PegasusForConditionalGeneration, PegasusTokenizer

tokenizer_model = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

loaded_model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

text = "Von Willebrand Disease (VWD) which a glycoprotein crucial for platelet adhesion to the subendothelium after vascular injury. VWD include quantitative defects of VWF, either partial (type 1 with VWF levels < 50 IU/dL) or virtually total (type 3 with undetectable VWF levels) and also qualitative defects of VWF (type 2 variants with discrepant antigenic and functional VWF levels). The most bleeding forms of VWD usually do not concern type 1 patients with the mildest VWF defects (VWF levels between 30 and 50IU/dL). Von willebrand factor is a complex multimeric protein with two functions: it forms a bridge between the platelets and areas of vascular damage and it binds to and stabilizes factor VIII, which is necessary for the clotting cascade. By taking a clinical history of bleeding (mucocutaneous bleeding symptoms suggestive of a primary haemostatic disorder, a quantitative or qualitative abnormality of VWF is possible) it is important to think about VWD and to make the appropriate diagnosis. If the VWD is suspected diagnostic tests should include an activated partial thromboplastin time, bleeding time, factor VIII: C Ristocetin cofactor and vWF antigen. Additional testing of ristocetin induced plattlet adhesion (RIPA) the multimeric structure and collagen binding test and genanalysis allow diagnosing the different types of von. Willebrand Disease. The treatment of choice in mild forms is the synthetic agent desmopressin. In patients with severe type 1, type 2B, 2N and type 3 or in people who do not response to desmopressin, the appropriate treatment is a factor VIII concentrate that is rich of VWF. We report a case of infant in 27-month-old boy who had been referred due to haemorrhagic shock. His birth histories, his familie's social history and developmental milestones were unremarkable. He was born at full term with no antenatal or perinatal complications. Prior to the symptoms, the child was on a normal diet and was thriving appropriately. The child presented one days before his admission trauma to the inner face of the lower lip that caused an external acute bleeding loss. The laboratory data showed unfortunately, the most severe form of Von Willebrand's Disease; Type 3. The management was based on erythrocyte and fresh-frozen plasma (FFP) transfusions with administration of factor VII with good evolution."
print("Text:",text)
tokens = tokenizer_model(text, truncation=True, padding="longest", return_tensors="pt")
tokens
summary = loaded_model.generate(**tokens)
print("Summary:",summary)
tokenizer_model.decode(summary[0])

text ="Tourette Syndrome is a disorder characterized by tics. It typically begins in childhood and often improves in adult life. Tics are best described as voluntary movements made automatically so that volition is not ordinarily appreciated. There is frequently an urge, sometimes in the form of a specific sensory feeling (sensory tic), that precedes the tic. Patients say that they make the tic in order to reduce the urge, although shortly after the tic, the urge recurs. The sensory feeling may arise due to defective sensory habituation. Since tics relieve the urge, this can be considered rewarding, and repetition of this behavior may perpetuate the tic as a habit. Tourette Syndrome affects boys more than girls and is associated with attention deficit hyperactivity disorder and obsessive compulsive disorder. Although Tourette Syndrome often appears to be autosomal recessive in inheritance, it has been difficult to find any abnormal genes. There is a loss of inhibition in these patients and recent studies show abnormalities in brain GABA. Certainly there is also an abnormality in dopamine function and dopamine blocking agents are effective therapy. In severe drug-refractory patients, deep brain stimulation can be effective." 
print("Text:",text)
tokens = tokenizer_model(text, truncation=True, padding="longest", return_tensors="pt")
tokens
summary = loaded_model.generate(**tokens)
print("Summary:",summary)
tokenizer_model.decode(summary[0])

text = "Ankylosing spondylitis is associated with disability comparable to that of rheumatoid arthritis. Diagnosis should first focus on eliciting a history of nocturnal back pain, diurnal variation in symptoms with prolonged morning stiffness, and a good response to NSAID therapy. Physical examination is often unrevealing. Pelvic x-ray results are often normal in early disease. Magnetic resonance imaging is the most sensitive imaging technique for detecting early inflammatory lesions and should be considered when history supports the diagnosis but results of plain radiography are normal. When patients have failed at least two courses of NSAID therapy, anti-TNF(alpha)therapies are of proven benefit."
print("Text:",text)
tokens = tokenizer_model(text, truncation=True, padding="longest", return_tensors="pt")
tokens
summary = loaded_model.generate(**tokens)
print("Summary:",summary)
tokenizer_model.decode(summary[0])

text = "Charcot-Marie-Tooth (CMT) is the most prevalent category of inherited neuropathy. The most common inheritance pattern is autosomal dominant, though there also are X-linked and autosomal recessive subtypes. In addition to a variety of inheritance patterns, there are a myriad of genes associated with CMT, reflecting the heterogeneity of this disorder. Next generation sequencing (NGS) has expanded and simplified the diagnostic yield of genes/molecules underlying and/or associated with CMT, which is of paramount importance in providing a substrate for current and future targeted disease-modifying treatment options. Considerable research attention for disease-modifying therapy has been geared towards the most commonly encountered genetic mutations (PMP22, GJB1, MPZ, and MFN2). In this review, we highlight the clinical background, molecular understanding, and therapeutic investigations of these CMT subtypes, while also discussing therapeutic research pertinent to the remaining less common CMT subtypes."
print("Text:",text)
tokens = tokenizer_model(text, truncation=True, padding="longest", return_tensors="pt")
tokens
summary = loaded_model.generate(**tokens)
print("Summary:",summary)
tokenizer_model.decode(summary[0])

text = "Categorization of the Ehlers-Danlos syndromes began in the late 1960s and was formalized in the Berlin nosology. Over time, it became apparent that the diagnostic criteria established and published in 1988 did not discriminate adequately between the different types of Ehlers-Danlos syndromes or between Ehlers-Danlos syndromes and other phenotypically related conditions. In addition, elucidation of the molecular basis of several Ehlers-Danlos syndromes has added a new dimension to the characterization of this group of disorders. We propose a revision of the classification of the Ehlers-Danlos syndromes based primarily on the cause of each type. Major and minor diagnostic criteria have been defined for each type and complemented whenever possible with laboratory findings. This simplified classification will facilitate an accurate diagnosis of the Ehlers-Danlos syndromes and contribute to the delineation of phenotypically related disordersEfforts on recognition, diagnosis, and management of the presumed, most common connective tissue disorder hypermobile Ehlers-Danlos syndrome have been an ongoing challenge, even decades after the description of this condition. A recent international consortium proposed a revised Ehlers-Danlos syndrome classification, an update much needed since Villefranche nosology, in 1998. Hypermobile Ehlers-Danlos syndrome is the only subtype in these groups of syndromes with no known genetic cause(s). This effort brought significant attention to this often underappreciated condition. This review provides an update of the clinical and genetic aspects of hypermobile Ehlers-Danlos syndrome for clinicians and researchers."
print("Text:",text)
tokens = tokenizer_model(text, truncation=True, padding="longest", return_tensors="pt")
tokens
summary = loaded_model.generate(**tokens)
print("Summary:",summary)
tokenizer_model.decode(summary[0])