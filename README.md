# Terrier Experimental Data

This repository contains the data for the application of Terrier to experimental data.

There are 8 flatworms. See the following directories:

 - flatworms/Clonorchis_sinensis
 - flatworms/Dicrocoelium_dendriticum
 - flatworms/Fasciola_hepatica
 - flatworms/Fasciolopsis_buski
 - flatworms/Schistosoma_haematobium
 - flatworms/Schistosoma_japonicum
 - flatworms/Schistosoma_mansoni
 - flatworms/Trichobilharzia_regenti

There are 51 amphibians:

 - amphibians/Allobates_femoralis
 - amphibians/Ambystoma_mexicanum
 - amphibians/Bombina_bombina
 - amphibians/Bombina_variegata
 - amphibians/Bufo_bufo
 - amphibians/Bufo_gargarizans
 - amphibians/Dendropsophus_ebraccatus
 - amphibians/Discoglossus_pictus
 - amphibians/Eleutherodactylus_coqui
 - amphibians/Engystomops_pustulosus
 - amphibians/Gastrophryne_carolinensis
 - amphibians/Geotrypetes_seraphini
 - amphibians/Glandirana_rugosa
 - amphibians/Hyalinobatrachium_fleischmanni
 - amphibians/Hyla_sarda
 - amphibians/Hymenochirus_boettgeri
 - amphibians/Leptobrachium_ailaonicum
 - amphibians/Leptobrachium_leishanense
 - amphibians/Leptodactylus_fallax
 - amphibians/Limnodynastes_dumerilii
 - amphibians/Lithobates_catesbeianus
 - amphibians/Lithobates_sylvaticus
 - amphibians/Mantella_aurantiaca
 - amphibians/Microcaecilia_unicolor
 - amphibians/Nanorana_parkeri
 - amphibians/Oophaga_pumilio
 - amphibians/Oophaga_sylvatica
 - amphibians/Pelobates_cultripes
 - amphibians/Phrynoglossus_myanhessei
 - amphibians/Phyllomedusa_bahiana
 - amphibians/Pipa_carvalhoi
 - amphibians/Pipa_parva
 - amphibians/Platyplectrum_ornatum
 - amphibians/Pleurodeles_waltl
 - amphibians/Pseudophryne_corroboree
 - amphibians/Pyxicephalus_adspersus
 - amphibians/Rana_kukunoris
 - amphibians/Rana_muscosa
 - amphibians/Rana_temporaria
 - amphibians/Ranitomeya_imitator
 - amphibians/Rhinatrema_bivittatum
 - amphibians/Rhinella_marina
 - amphibians/Scaphiopus_couchii
 - amphibians/Scaphiopus_holbrookii
 - amphibians/Spea_bombifrons
 - amphibians/Spea_hammondii
 - amphibians/Spea_multiplicata
 - amphibians/Staurois_parvus
 - amphibians/Xenopus_borealis
 - amphibians/Xenopus_laevis
 - amphibians/Xenopus_tropicalis

Each directory contains:

 - a FASTA file with extension .fa with the library of TE sequences.
 - a CSV file with the predictions from Terrier
 - a plot compairing the Terrier predictions with the original annotations (XXX-comparison.png)
 - a plot with the confusion matrix base on the original annotations (XXX-confusion.png)

To recreate the comparison plots, run this bash loop:

```bash

for CSV in $(find . -name '*.csv'); do
    terrier-tools comparison-plot \
        --csv $CSV  \
        --output ${CSV/.csv/-comparison.png} \
        --threshold 0.9 \
        --no-superfamily \
        --no-show
done
```

To recreate the confusion matrices, run this bash loop:

```bash
for CSV in $(find . -name '*.csv'); do
    terrier-tools confusion-matrix \
        --csv $CSV  \
        --output ${CSV/.csv/-confusion.png} \
        --threshold 0.9 \
        --no-superfamily \
        --no-show
done
```

To reproduce the Terrier CSV results, run the following bash loop:

```bash
for FASTA in $(find . -name '*.fa'); do
    terrier \
        --file $FASTA \
        --output-csv ${FASTA/.fa/.csv} \
        --threshold 0.0
done
```

To reproduce the comparison plot in the Terrier paper, run:

```bash

terrier-tools comparison-plot \
    --csv flatworms/Dicrocoelium_dendriticum/Dicrocoelium_dendriticum.csv  \
    --csv flatworms/Fasciola_hepatica/Fasciola_hepatica.csv  \
    --csv amphibians/Lithobates_catesbeianus/Lithobates_catesbeianus.csv  \
    --csv amphibians/Glandirana_rugosa/Glandirana_rugosa.csv  \
    --output comparison-big4.pdf \
    --threshold 0.9 \
    --no-superfamily
```


## Credits

Created by the Terrier team at the University of Melbourne.

If you use this dataset, cite the Terrier paper when it comes out.