MUSIC_HTML = """<script>
(function(){
    var AC = window.AudioContext || window.webkitAudioContext;
    if(!AC) return;
    var ctx = new AC();

    /* ── CADENA DE AUDIO ── */
    /* Compresor → evita clips */
    var comp = ctx.createDynamicsCompressor();
    comp.threshold.value = -18;
    comp.knee.value      =   8;
    comp.ratio.value     =   5;
    comp.attack.value    = 0.003;
    comp.release.value   = 0.15;
    comp.connect(ctx.destination);

    /* Reverb suave con dos delays en paralelo */
    function makeReverb(wetGain){
        var d1 = ctx.createDelay(1); d1.delayTime.value = 0.06;
        var d2 = ctx.createDelay(1); d2.delayTime.value = 0.11;
        var g1 = ctx.createGain(); g1.gain.value = wetGain * 0.5;
        var g2 = ctx.createGain(); g2.gain.value = wetGain * 0.3;
        d1.connect(g1); d1.connect(d2);
        d2.connect(g2);
        return { input:d1, outputs:[g1,g2] };
    }

    /* Master gain */
    var master = ctx.createGain();
    master.gain.value = 0.38;
    master.connect(comp);

    /* Reverb solo para melodía */
    var rev = makeReverb(0.18);
    rev.outputs.forEach(function(g){ g.connect(master); });

    /* Filtro pasa-bajos — suaviza el crunch del pulse */
    var lpf = ctx.createBiquadFilter();
    lpf.type            = 'lowpass';
    lpf.frequency.value = 7800;
    lpf.Q.value         = 0.6;
    lpf.connect(master);

    /* ── ONDA PULSE 25 % (NES channel 1) ── */
    /* Fourier: imag[k] = (4/(k·π)) · sin(0.5·k·π·duty) */
    var N = 64, real25 = new Float32Array(N), imag25 = new Float32Array(N);
    real25[0] = imag25[0] = 0;
    for(var k=1; k<N; k++){
        imag25[k] = (4/(k*Math.PI)) * Math.sin(0.5 * k * Math.PI * 0.25);
    }
    var pulse25 = ctx.createPeriodicWave(real25, imag25, {disableNormalization:false});

    /* ── TEMPO ── */
    var BPM=200, Q=60/BPM, E=Q/2, S=Q/4, H=Q*2, DQ=Q*1.5, DE=E*1.5;
    var R=0;

    /* ── FRECUENCIAS ── */
    var C3=130.81, E3=164.81, G3=196.00, C4=261.63, E4=329.63,
        G4=392.00, A4=440.00, Bb4=466.16, B4=493.88,
        C5=523.25, D5=587.33, E5=659.25, F5=698.46,
        G5=783.99, A5=880.00, Ab4=415.30, F4=349.23;

    /* ── MELODÍA (pulse 25 %) ── */
    var MEL=[
        /* INTRO HOOK */
        [E5,E],[R,E],[E5,E],[R,E],[C5,E],[E5,Q],[R,E],
        [G5,Q],[R,DQ],[G4,Q],[R,DQ],
        /* SECCIÓN A */
        [C5,E],[R,DQ],[G4,E],[R,DQ],[E4,E],[R,DQ],
        [A4,E],[R,E],[B4,E],[R,E],[Bb4,E],[A4,Q],[R,E],
        /* RUN 1 */
        [G4,S],[E5,S],[G5,S],[A5,E],[R,S],[F5,S],[G5,Q],
        [R,E],[E5,E],[R,E],[C5,E],[D5,E],[B4,DE],[R,E],
        /* RUN 2 */
        [G4,S],[E5,S],[G5,S],[A5,E],[R,S],[F5,S],[G5,Q],
        [R,E],[E5,E],[R,E],[C5,E],[D5,E],[B4,DE],[R,E],
        /* SECCIÓN B */
        [R,E],[Ab4,E],[R,E],[Ab4,E],[R,E],[Ab4,E],[R,E],
        [A4,E],[R,E],[A4,E],[Ab4,E],[A4,E],[R,E],
        [Bb4,E],[R,E],[B4,E],[R,E],
        [C5,E],[R,E],[C5,E],[B4,E],[C5,E],[R,E],
        [F5,E],[R,E],[E5,Q],[R,E],[C5,E],[A4,E],[G4,H],[R,H],
        /* INTRO HOOK reprise */
        [E5,E],[R,E],[E5,E],[R,E],[C5,E],[E5,Q],[R,E],
        [G5,Q],[R,DQ],[G4,Q],[R,DQ],
        /* SECCIÓN A reprise */
        [C5,E],[R,DQ],[G4,E],[R,DQ],[E4,E],[R,DQ],
        [A4,E],[R,E],[B4,E],[R,E],[Bb4,E],[A4,Q],[R,E],
        /* RUN FINAL */
        [G4,S],[E5,S],[G5,S],[A5,E],[R,S],[F5,S],[G5,Q],
        [R,E],[E5,E],[R,E],[C5,E],[D5,E],[B4,DE],[R,E],
        [G4,S],[E5,S],[G5,S],[A5,E],[R,S],[F5,S],[G5,Q],
        [R,E],[E5,E],[R,E],[C5,E],[D5,E],[B4,Q],[R,H]
    ];

    /* ── BAJO (triángulo, octava abajo) ── */
    /* Acompaña los acordes principales E / C / G / A */
    var BAS=[
        /* intro hook: E / C / G / G */
        [E4,E],[R,E],[E4,E],[R,E],[C4,E],[E4,Q],[R,E],[G4,Q],[R,DQ],[G3,Q],[R,DQ],
        /* sección A */
        [C4,E],[R,DQ],[G3,E],[R,DQ],[E3,E],[R,DQ],
        [A4,E],[R,E],[B4,E],[R,E],[Bb4,E],[A4,Q],[R,E],
        /* runs 1 y 2 */
        [C4,S],[E4,S],[G4,S],[A4,E],[R,S],[F4,S],[G4,Q],
        [R,E],[E4,E],[R,E],[C4,E],[D5,E],[B4,DE],[R,E],
        [C4,S],[E4,S],[G4,S],[A4,E],[R,S],[F4,S],[G4,Q],
        [R,E],[E4,E],[R,E],[C4,E],[D5,E],[B4,DE],[R,E],
        /* sección B */
        [R,E],[Ab4,E],[R,E],[Ab4,E],[R,E],[Ab4,E],[R,E],
        [A4,E],[R,E],[A4,E],[Ab4,E],[A4,E],[R,E],
        [Bb4,E],[R,E],[B4,E],[R,E],
        [C4,E],[R,E],[C4,E],[B4,E],[C4,E],[R,E],
        [F4,E],[R,E],[E4,Q],[R,E],[C4,E],[A4,E],[G3,H],[R,H],
        /* reprise */
        [E4,E],[R,E],[E4,E],[R,E],[C4,E],[E4,Q],[R,E],[G4,Q],[R,DQ],[G3,Q],[R,DQ],
        [C4,E],[R,DQ],[G3,E],[R,DQ],[E3,E],[R,DQ],
        [A4,E],[R,E],[B4,E],[R,E],[Bb4,E],[A4,Q],[R,E],
        [C4,S],[E4,S],[G4,S],[A4,E],[R,S],[F4,S],[G4,Q],
        [R,E],[E4,E],[R,E],[C4,E],[D5,E],[B4,DE],[R,E],
        [C4,S],[E4,S],[G4,S],[A4,E],[R,S],[F4,S],[G4,Q],
        [R,E],[E4,E],[R,E],[C4,E],[D5,E],[B4,Q],[R,H]
    ];

    /* ── FUNCIONES DE NOTA ── */
    function melNota(freq, tStart, dur){
        if(!freq) return;
        var osc = ctx.createOscillator();
        var env = ctx.createGain();
        osc.setPeriodicWave(pulse25);
        osc.frequency.value = freq;
        env.gain.setValueAtTime(0,   tStart);
        env.gain.linearRampToValueAtTime(0.75, tStart + 0.004);
        env.gain.setValueAtTime(0.75, tStart + dur * 0.72);
        env.gain.linearRampToValueAtTime(0,   tStart + dur * 0.94);
        osc.connect(env);
        env.connect(lpf);
        env.connect(rev.input);   /* reverb suave */
        osc.start(tStart); osc.stop(tStart + dur);
    }

    function basNota(freq, tStart, dur){
        if(!freq) return;
        var osc = ctx.createOscillator();
        var env = ctx.createGain();
        osc.type = 'triangle';    /* canal triángulo NES para el bajo */
        osc.frequency.value = freq;
        env.gain.setValueAtTime(0,   tStart);
        env.gain.linearRampToValueAtTime(0.45, tStart + 0.003);
        env.gain.setValueAtTime(0.45, tStart + dur * 0.80);
        env.gain.linearRampToValueAtTime(0,   tStart + dur * 0.96);
        osc.connect(env);
        env.connect(master);
        osc.start(tStart); osc.stop(tStart + dur);
    }

    /* ── LOOP ── */
    function loop(){
        var t = ctx.currentTime + 0.05;
        var lenM = MEL.length, lenB = BAS.length;
        var len  = Math.max(lenM, lenB);
        var tm = t, tb = t;
        for(var i=0; i<lenM; i++){
            melNota(MEL[i][0], tm, MEL[i][1]*0.88);
            tm += MEL[i][1];
        }
        for(var j=0; j<lenB; j++){
            basNota(BAS[j][0], tb, BAS[j][1]*0.88);
            tb += BAS[j][1];
        }
        var total = Math.max(tm, tb);
        setTimeout(loop, (total - ctx.currentTime - 0.04) * 1000);
    }

    function start(){ ctx.resume().then(loop); }
    if(ctx.state === 'running'){ loop(); }
    else { ctx.resume().then(loop).catch(function(){
        document.addEventListener('click', start, {once:true});
    }); }
})();
</script>"""
