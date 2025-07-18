# Terrier Experimental Data

This repository contains the data for the application of [Terrier](https://github.com/rbturnbull/terrier) to experimental data.

There are 8 libraries of transposable elements (TEs) from flatworms. See the following directories:

 - flatworms/Clonorchis_sinensis
 - flatworms/Dicrocoelium_dendriticum
 - flatworms/Fasciola_hepatica
 - flatworms/Fasciolopsis_buski
 - flatworms/Schistosoma_haematobium
 - flatworms/Schistosoma_japonicum
 - flatworms/Schistosoma_mansoni
 - flatworms/Trichobilharzia_regenti

Schistosoma mansoni also has a FASTA file with 21 TEs annotated in the NCBI database.

There are 51 libraries of TEs from amphibians:

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

Most amphibian repeat libraries were generated using RepeatModeler version 2.0.4 (excluding the LTR pipeline extensions by Jullien M. Flynn). Ambistoma mexicanum was generated using RepeatModeler version 2.0.5.

Each directory contains:

 - a FASTA file with extension .fa with the library of TE sequences.
 - a CSV file with the predictions from Terrier
 - a plot comparing the Terrier predictions with the original annotations (XXXXXXX-comparison.png)
 - a plot with the confusion matrix base on the original annotations (XXXXXXX-confusion.png)

A summary CSV of the results is found in `summary.csv`.

To reproduce the plot in the paper from the summary, run `plot-summary.py`. This script requires the same virtual environment as Terrier.

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

To comparison plot of the two flatworms and the two amphibians with the most transposable elements, run:

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

The timings for the Terrier runs are found in `timings.csv`. To reproduce the plot of the timings, run `plot-timings.py`.

## Credits

Terrier was developed by:

- [Robert Turnbull](https://robturnbull.com)
- [Neil D. Young](https://findanexpert.unimelb.edu.au/profile/249669-neil-young)
- [Edoardo Tescari](https://findanexpert.unimelb.edu.au/profile/428364-edoardo-tescari)
- [Lee F. Skerratt](https://findanexpert.unimelb.edu.au/profile/451921-lee-skerratt)
- [Tiffany A. Kosch](https://findanexpert.unimelb.edu.au/profile/775927-tiffany-kosch)

If you use this dataset, cite the Terrier paper. See more information at: https://github.com/rbturnbull/terrier