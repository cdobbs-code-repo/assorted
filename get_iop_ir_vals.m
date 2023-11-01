

% 487E diff (Z2) script helper %

function [IOPA,IRTA,IOPB,IRTB,IOPC,IRTC] = get_iop_ir_vals(IAS_raw,IAS_angle,...
                                                           IBS_raw,IBS_angle,...
                                                           ICS_raw,ICS_angle,...
                                                           IAW_raw,IAW_angle,...
                                                           IBW_raw,IBW_angle,...
                                                           ICW_raw,ICW_angle,...
                                                           TAPS,TAPT,TAPU,...
                                                           TAPW,TAPX,TAPY)

    
    SLP1 = 35;
    SLP2 = 75;
    
    TSCTP = "N";
    TTCTP = "P";
    TUCTP = "P";
    TWCTP = "P";
    TXCTP = "P";
    TYCTP = "P";
    
    % IS pre-TAP
    IAS = IAS_raw/TAPS;
    if TSCTP == "N"
        IAS = -IAS;
    end
    IBS = IBS_raw/TAPS;
    if TSCTP == "N"
        IBS = -IBS;
    end
    ICS = ICS_raw/TAPS;
    if TSCTP == "N"
        ICS = -ICS;
    end
    % IT pre-TAP
    IAT_raw = IBS_raw;
    IAT = IAT_raw/TAPT;
    IAT_angle = IBS_angle;
    if TTCTP == "N"
        IAT = -IAT;
    end
    IBT_raw = ICS_raw;
    IBT = IBT_raw/TAPT;
    IBT_angle = ICS_angle;
    if TTCTP == "N"
        IBT = -IBT;
    end
    ICT_raw = IAS_raw;
    ICT = ICT_raw/TAPT;
    ICT_angle = IAS_angle;
    if TTCTP == "N"
        ICT = -ICT;
    end
    % IU pre-TAP
    IAU_raw = ICS_raw;
    IAU = IAU_raw/TAPU;
    IAU_angle = ICS_angle;
    if TUCTP == "N"
        IAU = -IAU;
    end
    IBU_raw = IAS_raw;
    IBU = IBU_raw/TAPU;
    IBU_angle = IAS_angle;
    if TUCTP == "N"
        IBU = -IBU;
    end
    ICU_raw = IBS_raw;
    ICU = ICU_raw/TAPU;
    ICU_angle = IBS_angle;
    if TUCTP == "N"
        ICU = -ICU;
    end
    % IW pre-TAP
    IAW = IAW_raw/TAPW;
    if TWCTP == "N"
        IAW = -IAW;
    end
    IBW = IBW_raw/TAPW;
    if TWCTP == "N"
        IBW = -IBW;
    end
    ICW = ICW_raw/TAPW;
    if TWCTP == "N"
        ICW = -ICW;
    end
    % IX pre-TAP
    IAX_raw = IBW_raw;
    IAX = IAX_raw/TAPX;
    IAX_angle = IBW_angle;
    if TXCTP == "N"
        IAX = -IAX;
    end
    IBX_raw = ICW_raw;
    IBX = IBX_raw/TAPX;
    IBX_angle = ICW_angle;
    if TXCTP == "N"
        IBX = -IBX;
    end
    ICX_raw = IAW_raw;
    ICX = ICX_raw/TAPX;
    ICX_angle = IAW_angle;
    if TXCTP == "N"
        ICX = -ICX;
    end
    % IY pre-TAP
    IAY_raw = ICW_raw;
    IAY = IAY_raw/TAPY;
    IAY_angle = ICW_angle;
    if TYCTP == "N"
        IAY = -IAY;
    end
    IBY_raw = IAW_raw;
    IBY = IBY_raw/TAPY;
    IBY_angle = IAW_angle;
    if TYCTP == "N"
        IBY = -IBY;
    end
    ICY_raw = IBW_raw;
    ICY = ICY_raw/TAPY;
    ICY_angle = IBW_angle;
    if TYCTP == "N"
        ICY = -ICY;
    end
    
    IOPA = IAS*exp(1j*IAS_angle*pi/180) + IAT*exp(1j*IAT_angle*pi/180) + IAU*exp(1j*IAU_angle*pi/180) + IAW*exp(1j*IAW_angle*pi/180) + IAX*exp(1j*IAX_angle*pi/180) + IAY*exp(1j*IAY_angle*pi/180);
    IOPA = sqrt(real(IOPA)*real(IOPA) + imag(IOPA)*imag(IOPA));
    IRTA = abs(IAS) + abs(IAT) + abs(IAU) + abs(IAW) + abs(IAX) + abs(IAY);
    
    IOPB = IBS*exp(1j*IBS_angle*pi/180) + IBT*exp(1j*IBT_angle*pi/180) + IBU*exp(1j*IBU_angle*pi/180) + IBW*exp(1j*IBW_angle*pi/180) + IBX*exp(1j*IBX_angle*pi/180) + IBY*exp(1j*IBY_angle*pi/180);
    IOPB = sqrt(real(IOPB)*real(IOPB) + imag(IOPB)*imag(IOPB));
    IRTB = abs(IBS) + abs(IBT) + abs(IBU) + abs(IBW) + abs(IBX) + abs(IBY);
    
    IOPC = ICS*exp(1j*ICS_angle*pi/180) + ICT*exp(1j*ICT_angle*pi/180) + ICU*exp(1j*ICU_angle*pi/180) + ICW*exp(1j*ICW_angle*pi/180) + ICX*exp(1j*ICX_angle*pi/180) + ICY*exp(1j*ICY_angle*pi/180);
    IOPC = sqrt(real(IOPC)*real(IOPC) + imag(IOPC)*imag(IOPC));
    IRTC = abs(ICS) + abs(ICT) + abs(ICU) + abs(ICW) + abs(ICX) + abs(ICY);
    
end













