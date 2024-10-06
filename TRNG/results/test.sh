
for i in {0..15}; do
    mkdir -p $i
    cd $i
    ../../sts/sts -i 5 -F a -s ../../data-$i.txt
    cd ..
done
