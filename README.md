<a name="readme-top"></a>



<!-- PROJECT LOGO -->
<div align="center">


  <h2 align="center">
    Bigram Language Model
  </h2>
</div>




<div>
<div align="center">
    <img src="images/bigram-probabilities.png" alt="Logo" width="400">
</div>

<br/>
<br/>

Basic probablistic language model<br/>
Next char probabilities are calculated from a dataset.
<br/>
Model can generate approximately similar terms.
<br/>
<br/>
The resulting ouputs demonstrate the limitations of a bigram model, and expending the model's context would result in exponential growth (27<sup>n</sup>) of the probability table. 
<br/>
This 2-character context model has 729 possible contexts; if the model were scaled to 3 character context, the probability table would grow to 19,683 contexts.
</div>

Example name generation:
<br/>
_Sia_
<br/>
_Elari_
<br/>
_Zaronami_
<br/>
_Kylauni_


<!-- GETTING STARTED -->

## Usage

Clone the repo
   ```sh
   git clone https://github.com/ryansereno/bigram
   ```
Run
   ```sh
   python model.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>










