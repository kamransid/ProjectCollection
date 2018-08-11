public enum EnumTest {
    BUSINESS_ERROR(100), SERVER_ERROR(500), NETWORK_ERROR(1000);
    private int errorCode;
    private EnumTest(int errorCode) {
    this.errorCode = errorCode;
    }
    public int getErrorCode() {
    return errorCode;
    }
}