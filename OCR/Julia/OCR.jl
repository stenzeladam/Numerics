using PyPlot
using Random

# Implement an artificial neural netword for Optical Character Recognition (OCR). 
# Use multilayer perceptron (MLP) with a single hidden layer

# Custom show function for matrices, making it easier to read them in print() calls
Base.show(io::IO, m::AbstractMatrix) = print_matrix(io, m)

function print_matrix(io::IO, m::AbstractMatrix)
    for row in eachrow(m)
        println(io, row)
    end
end

charstr = """
          OOOOOO  OOOOOO  OOOOOO  OO..OO
          OOOOOO  OOOOOO  OOOOOO  OO..OO
          O.OO.O  OO..OO  ..OO..  OO..OO
          O.OO.O  OO..OO  ..OO..  OOOOOO
          O....O  OOOOOO  ..OO..  OO..OO
          O....O  OO..OO  ..OO..  OO..OO
          O... O  OO..OO  ..OO..  OO..OO
          """

# training is a size 42 x 4 array contianing the 42 pixel-values for each of the 4 characters
# target is a size 2 x 4 array containing the desired output for each of the 4 characters
# mapstr is the string "MATH" which is the characters that each target output corresponds to 

training = reshape(collect(charstr), :, 7) 
training = Int.(training[[1:6;9:14;17:22;25:30],:] .== 'O')
training = reshape(training', 7*6, 4)

target = [0 0; 0 1; 1 0; 1 1]'

mapstr = "MATH";

function plot_chars(images)
    gray()
    n_images = size(images,2)
    for j = 1:n_images
        subplot(ceil(Int, n_images/4), 4, j)
        im = 1 .- reshape(images[:,j], 7, 6)
        imshow(im); axis("off");
    end
end
#plot_chars(training)
#show()

# Now need to generate noisy test characters to test the trained OCR code. Modify the true character images in training

function make_testdata(training)
    testdata = zeros(42, 20)
    testdata[:, 1:4] .= training
    println(testdata)
    for i = 1:4
        numberPixelsChange = 2*i
        img = training
        for j = 1:4
            jthLetter = img[:, j]
            indicesToFlip = shuffle(1:42)[1:numberPixelsChange]
            for index in indicesToFlip
                jthLetter[index] = jthLetter[index] == 0 ? 1 : 0 # Flips the value from 0 to 1, and vice versa
            end
            columnAffected = 5 + (i - 1) * 4 + (j - 1)
            testdata[:, columnAffected] = jthLetter
        end
    end
    return testdata
end

testdata = make_testdata(training);
plot_chars(testdata)
#show()