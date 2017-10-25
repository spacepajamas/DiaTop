function gettopicDetails() {
	var toData = document.getElementById("to2").value;
	var fromData = document.getElementById("from2").value;
	var e = document.getElementById("topiclist");
	var strUser = e.options[e.selectedIndex].value;

	if (strUser == 0) {
		alert('Please select at least one topic from the drop down list.')
	} else {
		var horX = horaxis.slice(toData - 1990, fromData - 1989);
		horX.unshift('x')
		if (e.options[e.selectedIndex].value == 'Topic 13') {
			//var topic1 =  [ 0.00416812,  0.00417095,  0.00934077,  0.00742919,  0.00504197,0.00945139,  0.00838525,  0.00843802,  0.00571157,  0.00294206,  0.00903198,  0.00288118,  0.00490719,  0.00896932,  0.00180692]
			var slicedt1w1 = woman.slice(toData - 1990, fromData - 1989);
			slicedt1w1.unshift('woman')
			var slicedt1w2 = heart.slice(toData - 1990, fromData - 1989);
			slicedt1w2.unshift('heart')
			var slicedt1w3 = pregnancy.slice(toData - 1990, fromData - 1989);
			slicedt1w3.unshift('pregnancy')
			var slicedt1w4 = pressure.slice(toData - 1990, fromData - 1989);
			slicedt1w4.unshift('pressure')
			var slicedt1w5 = birth.slice(toData - 1990, fromData - 1989);
			slicedt1w5.unshift('birth')
			var slicedt1w6 = infant.slice(toData - 1990, fromData - 1989);
			slicedt1w6.unshift('infant')
			var slicedt1w7 = delivery.slice(toData - 1990, fromData - 1989);
			slicedt1w7.unshift('delivery')
			var slicedt1w8 = hypertension.slice(toData - 1990, fromData - 1989);
			slicedt1w8.unshift('hypertension')
			var slicedt1w9 = mother.slice(toData - 1990, fromData - 1989);
			slicedt1w9.unshift('mother')
			var slicedt1w10 = week.slice(toData - 1990, fromData - 1989);
			slicedt1w10.unshift('week')
			var chart = c3.generate({
				bindto: '#demo2',
				data: {
					x: 'x',
					columns: [horX, slicedt1w1, slicedt1w2, slicedt1w3, slicedt1w4, slicedt1w5, slicedt1w6, slicedt1w7, slicedt1w8, slicedt1w9, slicedt1w10]
				}
			});
		}
		if (e.options[e.selectedIndex].value == 'Topic 22') { //var testvar = topicwordslist.infection
			//document.getElementById("demo").innerHTML = typeof(testvar);
			//alert(testvar);
			//var topic1 =  [ 0.00416812,  0.00417095,  0.00934077,  0.00742919,  0.00504197,0.00945139,  0.00838525,  0.00843802,  0.00571157,  0.00294206,  0.00903198,  0.00288118,  0.00490719,  0.00896932,  0.00180692]
			var slicedt1w1 = topicwordslist.infection.slice(toData - 1990, fromData - 1989);
			slicedt1w1.unshift('infection')
			var slicedt1w2 = topicwordslist.virus.slice(toData - 1990, fromData - 1989);
			slicedt1w2.unshift('virus')
			var slicedt1w3 = topicwordslist.vaccine.slice(toData - 1990, fromData - 1989);
			slicedt1w3.unshift('vaccine')
			var slicedt1w4 = topicwordslist.antibody.slice(toData - 1990, fromData - 1989);
			slicedt1w4.unshift('antibody')
			var slicedt1w5 = topicwordslist.vaccination.slice(toData - 1990, fromData - 1989);
			slicedt1w5.unshift('vaccination')
			var slicedt1w6 = topicwordslist.antigen.slice(toData - 1990, fromData - 1989);
			slicedt1w6.unshift('antigen')
			var slicedt1w7 = topicwordslist.replication.slice(toData - 1990, fromData - 1989);
			slicedt1w7.unshift('replication')
			var slicedt1w8 = topicwordslist.titer.slice(toData - 1990, fromData - 1989);
			slicedt1w8.unshift('titer')
			var slicedt1w9 = topicwordslist.influenza.slice(toData - 1990, fromData - 1989);
			slicedt1w9.unshift('influenza')
			var slicedt1w10 = topicwordslist.transmission.slice(toData - 1990, fromData - 1989);
			slicedt1w10.unshift('transmission')
			var chart = c3.generate({
				bindto: '#demo2',
				data: {
					x: 'x',
					columns: [horX, slicedt1w1, slicedt1w2, slicedt1w3, slicedt1w4, slicedt1w5, slicedt1w6, slicedt1w7, slicedt1w8, slicedt1w9, slicedt1w10]
				}
			});
		}
		//else  { var slicedtopic1 = [];} 
		if (e.options[e.selectedIndex].value == 'Topic 34') { //var testvar = topicwordslist.infection

			var slicedt1w1 = topicwordslist.cancer.slice(toData - 1990, fromData - 1989);
			slicedt1w1.unshift('cancer')
			var slicedt1w2 = topicwordslist.tumor.slice(toData - 1990, fromData - 1989);
			slicedt1w2.unshift('tumor')
			var slicedt1w3 = topicwordslist.breast.slice(toData - 1990, fromData - 1989);
			slicedt1w3.unshift('breast')
			var slicedt1w4 = topicwordslist.antibody.slice(toData - 1990, fromData - 1989);
			slicedt1w4.unshift('antibody')
			var slicedt1w5 = topicwordslist.survival.slice(toData - 1990, fromData - 1989);
			slicedt1w5.unshift('survival')
			var slicedt1w6 = topicwordslist.metastasis.slice(toData - 1990, fromData - 1989);
			slicedt1w6.unshift('metastasis')
			var slicedt1w7 = topicwordslist.growth.slice(toData - 1990, fromData - 1989);
			slicedt1w7.unshift('growth')
			var slicedt1w8 = topicwordslist.lung.slice(toData - 1990, fromData - 1989);
			slicedt1w8.unshift('lung')
			var slicedt1w9 = topicwordslist.tumour.slice(toData - 1990, fromData - 1989);
			slicedt1w9.unshift('tumour')
			var slicedt1w10 = topicwordslist.chemotherapy.slice(toData - 1990, fromData - 1989);
			slicedt1w10.unshift('chemotherapy')
			var chart = c3.generate({
				bindto: '#demo2',
				data: {
					x: 'x',
					columns: [horX, slicedt1w1, slicedt1w2, slicedt1w3, slicedt1w4, slicedt1w5, slicedt1w6, slicedt1w7, slicedt1w8, slicedt1w9, slicedt1w10]
				}
			});
		}
		if (e.options[e.selectedIndex].value == 'Topic 38') { //var testvar = topicwordslist.infection

			var slicedt1w1 = topicwordslist.infection.slice(toData - 1990, fromData - 1989);
			slicedt1w1.unshift('infection')
			var slicedt1w2 = topicwordslist.resistance.slice(toData - 1990, fromData - 1989);
			slicedt1w2.unshift('resistance')
			var slicedt1w3 = topicwordslist.bacteria.slice(toData - 1990, fromData - 1989);
			slicedt1w3.unshift('bacteria')
			var slicedt1w4 = topicwordslist.isolates.slice(toData - 1990, fromData - 1989);
			slicedt1w4.unshift('isolates')
			var slicedt1w5 = topicwordslist.strain.slice(toData - 1990, fromData - 1989);
			slicedt1w5.unshift('strain')
			var slicedt1w6 = topicwordslist.culture.slice(toData - 1990, fromData - 1989);
			slicedt1w6.unshift('culture')
			var slicedt1w7 = topicwordslist.pathogen.slice(toData - 1990, fromData - 1989);
			slicedt1w7.unshift('pathogen')
			var slicedt1w8 = topicwordslist.phage.slice(toData - 1990, fromData - 1989);
			slicedt1w8.unshift('phage')
			var slicedt1w9 = topicwordslist.tuberculosis.slice(toData - 1990, fromData - 1989);
			slicedt1w9.unshift('tuberculosis')
			var slicedt1w10 = topicwordslist.coli.slice(toData - 1990, fromData - 1989);
			slicedt1w10.unshift('coli')
			var chart = c3.generate({
				bindto: '#demo2',
				data: {
					x: 'x',
					columns: [horX, slicedt1w1, slicedt1w2, slicedt1w3, slicedt1w4, slicedt1w5, slicedt1w6, slicedt1w7, slicedt1w8, slicedt1w9, slicedt1w10]
				}
			});
		}
		////////
		document.getElementById("demo").innerHTML = 'now displaying results for ' + strUser;
	}
}



var woman = [0.012448132780100001, 0.0, 0.0063492063492099999, 0.010101010100999999, 0.015974440894599998, 0.0239361702128, 0.017283950617299999, 0.024691358024699999, 0.046255506607900003, 0.050847457627099996, 0.085245901639300001, 0.122919334187, 0.151696606786, 0.165635738832, 0.18045501551199999, 0.16277258567, 0.15431952662699999, 0.170424750918, 0.17888487351599999, 0.17147980370000002, 0.17617779024099997, 0.17272778688999998, 0.17622283909299999, 0.172167744628, 0.178772802653]
var heart = [0.0041493775933600001, 0.0, 0.00952380952381, 0.010101010100999999, 0.0063897763578300007, 0.063829787233999999, 0.066666666666699986, 0.054320987654300004, 0.063876651982400001, 0.076271186440699995, 0.077049180327899994, 0.084507042253500003, 0.111776447106, 0.12508591065300001, 0.129265770424, 0.13317757009299999, 0.12023668639100001, 0.13651459534999999, 0.14300464635999999, 0.14496036240099999, 0.14406898485700001, 0.14959561110799999, 0.147315018666, 0.15255581055700002, 0.150995024876]
var pregnancy = [0.0041493775933600001, 0.0, 0.0063492063492099999, 0.0033670033669999998, 0.00319488817891, 0.00265957446809, 0.014814814814799999, 0.017283950617299999, 0.015418502202600002, 0.015254237288100001, 0.016393442623, 0.035851472471199998, 0.048902195608800006, 0.047422680412400005, 0.046535677352599995, 0.047897196261699998, 0.045917159763299999, 0.050865233350800003, 0.058208569953500003, 0.058135145337899999, 0.058679192372399998, 0.059498897121199996, 0.061309466832600003, 0.05704151888169999, 0.060240464344899998]
var pressure = [0.0082987551867200002, 0.0, 0.0031746031746000001, 0.010101010100999999, 0.015974440894599998, 0.0585106382979, 0.046913580246900004, 0.064197530864199992, 0.068281938326000005, 0.074576271186399992, 0.072131147541000001, 0.121638924456, 0.14171656686600001, 0.14707903780099998, 0.17166494312300001, 0.17679127725900001, 0.180355029586, 0.19157489949299999, 0.19463087248300001, 0.20347300868299997, 0.20120583286600002, 0.207624003167, 0.207140805973, 0.21472981431300001, 0.217868988391]
var birth = [0.0082987551867200002, 0.0, 0.0031746031746000001, 0.0, 0.0063897763578300007, 0.0159574468085, 0.0271604938272, 0.014814814814799999, 0.028634361233500001, 0.018644067796599998, 0.029508196721299999, 0.034571062740099995, 0.055888223552900004, 0.064604810996599996, 0.0620475698035, 0.071261682243000002, 0.056568047337300004, 0.063800034958899993, 0.067630356220999999, 0.072385805964500005, 0.065689848569800008, 0.071036706068699995, 0.071408059730100004, 0.0654287502608, 0.07259535655060001]
var hypertension = [0.0082987551867200002, 0.0, 0.0063492063492099999, 0.016835016835000001, 0.00319488817891, 0.00265957446809, 0.014814814814799999, 0.0123456790123, 0.015418502202600002, 0.028813559322000002, 0.022950819672099998, 0.047375160051200002, 0.053892215568900004, 0.052233676975899999, 0.068769389865600009, 0.065420560747700002, 0.072662721893499996, 0.069393462681300006, 0.081311306143500003, 0.082861457153600007, 0.0833567021873, 0.086986030201899989, 0.086005551833100005, 0.087460880450699996, 0.090961857379800004]
var infant = [0.0041493775933600001, 0.0, 0.0, 0.0033670033669999998, 0.00319488817891, 0.0053191489361699993, 0.0049382716049399993, 0.0074074074074099994, 0.013215859030799998, 0.0050847457627100001, 0.016393442623, 0.0140845070423, 0.019960079840299998, 0.030927835051499999, 0.031540847983500001, 0.034657320872300001, 0.029112426035500003, 0.0298898793917, 0.035363964894199997, 0.036995092487699992, 0.034772854739199999, 0.0337650585374, 0.035129702306900004, 0.033465470477799998, 0.036525704809300001]
var delivery = [0.012448132780100001, 0.0035211267605599998, 0.0063492063492099999, 0.0067340067340100002, 0.0095846645367399994, 0.0585106382979, 0.032098765432099996, 0.032098765432099996, 0.052863436123300002, 0.059322033898300007, 0.075409836065600006, 0.075544174135699999, 0.077844311377200007, 0.080412371134000002, 0.085832471561500007, 0.09540498442369999, 0.080946745562100006, 0.094913476664899993, 0.098864223025299999, 0.102585881465, 0.10726303982100001, 0.10712063797299999, 0.10993586675599999, 0.109743375756, 0.11285240464299999]
var mother = [0.0041493775933600001, 0.0, 0.0, 0.0, 0.00319488817891, 0.0239361702128, 0.029629629629599998, 0.0123456790123, 0.0088105726872199988, 0.018644067796599998, 0.024590163934400004, 0.033290653008999999, 0.032934131736499998, 0.0460481099656, 0.0480868665977, 0.047897196261699998, 0.046390532544400002, 0.047194546407999999, 0.050593701600400005, 0.048886372215900004, 0.047742568704399996, 0.048300435495699998, 0.0499186369293, 0.046442728979800001, 0.050082918739599996]
var week = [0.0041493775933600001, 0.0035211267605599998, 0.0126984126984, 0.013468013467999999, 0.00319488817891, 0.071808510638300002, 0.046913580246900004, 0.056790123456800005, 0.09471365638769999, 0.083050847457599997, 0.14754098360699999, 0.176696542894, 0.22155688622799999, 0.19656357388300003, 0.23888314374400002, 0.26557632398800002, 0.26603550295899997, 0.27285439608500001, 0.29155911202899998, 0.29577198943000005, 0.30545429052200002, 0.30320683219300004, 0.31032832392100002, 0.30811600250400001, 0.32276119403000003]
